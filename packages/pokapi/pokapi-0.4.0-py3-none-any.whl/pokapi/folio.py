'''
folio.py: Interface to FOLIO

Authors
-------

Michael Hucka <mhucka@caltech.edu> -- Caltech Library

Copyright
---------

Copyright (c) 2021-2023 by the California Institute of Technology.  This code
is open-source software released under a 3-clause BSD license.  Please see the
file "LICENSE" for more information.
'''

from   commonpy.exceptions import NoContent, RateLimitExceeded, AuthenticationFailure
from   commonpy.interrupt import wait
from   commonpy.string_utils import antiformat
from   commonpy.network_utils import net
import json
import regex

if __debug__:
    from sidetrack import log

from .exceptions import FolioError, FolioPermissionError, NotFound
from .record import FolioRecord


# Internal constants.
# .............................................................................

# Time in seconds we pause if we hit the rate limit, and number of times we
# repeatedly wait before we give up entirely.
_RATE_LIMIT_SLEEP = 15
_MAX_SLEEP_CYCLES = 8

# URL templates for retrieving data from a FOLIO/Okapi server.
_INSTANCE_FOR_BARCODE = '{}/inventory/instances?query=item.barcode%3D%3D{}'
_INSTANCE_FOR_INSTANCE_ID = '{}/instance-storage/instances/{}'

# Type identifiers for some things we look for.
_TYPE_ID_ISBN = '8261054f-be78-422d-bd51-4ed9f33c3422'
_TYPE_ID_ISSN = '913300b2-03ed-469a-8179-c1092c991227'


# Class definitions.
# .............................................................................

class Folio():
    '''Interface to a FOLIO server using Okapi.'''

    def __init__(self, okapi_url, okapi_token, tenant_id, an_prefix):
        '''Create an interface to the Folio server at "okapi_url".

        The parameters define certain things Pokapi can't get on its own.
        These are: the the Okapi URL for your instance, an Okapi API token, a
        tenant id, and the prefix that appears in front of your accession
        numbers.  (As an example of a prefix for accession numbers, for
        Caltech the prefix is the 'clc' part of an accession number such as
        'clc.025d49d5.735a.4d79.8889.c5895ac65fd2'.)
        '''

        self.okapi_url = okapi_url
        self.okapi_token = okapi_token
        self.tenant_id = tenant_id
        self.an_prefix = an_prefix


    def record(self, barcode = None, accession_number = None, instance_id = None,
               raw_json = None):
        '''Create a FolioRecord object.

        The arguments are mutually exclusive; callers must supply only one
        of the following:

          * 'barcode': retrieve the record corresponding to the given item
            barcode

          * 'instance_id': retrieve the record having the given FOLIO
            instance identifier

          * 'accession_number': retrieve the record corresponding to the
            accession number

          * 'raw_json': (for advanced uses) the JSON content returned by
            FOLIO for an instance record, for example from a past call

        This contacts the FOLIO server and perform a search using the given
        identifier, then creates a FolioRecord object and returns it.  If
        the FOLIO server does not return a result, this method raises a
        NotFound exception.

        If no argument is given, this returns an empty FolioRecord.
        '''

        args = [barcode, accession_number, instance_id, raw_json]
        if sum(map(bool, args)) > 1:
            raise ValueError('Keyword args to record() are mutually exclusive.')
        if barcode:
            return self._record_from_server(_INSTANCE_FOR_BARCODE, barcode)
        elif accession_number:
            # Accession numbers are based on instance id's.
            instance_id = id_from_an(accession_number)
            return self._record_from_server(_INSTANCE_FOR_INSTANCE_ID, instance_id)
        elif instance_id:
            return self._record_from_server(_INSTANCE_FOR_INSTANCE_ID, instance_id)
        elif raw_json:
            return self._record_from_server(raw_json = raw_json)
        else:
            return FolioRecord()


    def _record_from_server(self, url_template = None, identifier = None,
                            raw_json = None):
        '''Create a FolioRecord object from data returned by the server.

        Callers should either provide a value for both "url_template" and
        "identifier", OR a value for "raw_json".  If the latter, the value
        should be instance data as JSON returned by FOLIO OKAPI.  This is
        useful when testing, and may be useful if callers cache the values.
        '''

        def response_handler(resp):
            if not resp or not resp.text:
                if __debug__: log(f'FOLIO returned no result for {request_url}')
                return None
            data_dict = json.loads(resp.text)
            # Depending on the way we're getting it, the record might be
            # directly provided or it might be in a list of records.
            if 'totalRecords' not in data_dict:
                if 'title' in data_dict:
                    # It's a record directly and not a list of records.
                    return data_dict
                else:
                    raise FolioError('Unexpected data returned by FOLIO')
            elif data_dict['totalRecords'] == 0:
                if __debug__: log(f'got 0 records for {request_url}')
                return None
            elif data_dict['totalRecords'] > 1:
                total = data_dict['totalRecords']
                if __debug__: log(f'got {total} records for {request_url}')
                if __debug__: log('using only first value')
            return data_dict['instances'][0]

        if raw_json:
            if isinstance(raw_json, str):
                json_dict = json.loads(raw_json)
            elif isinstance(raw_json, dict):
                json_dict = raw_json
            else:
                raise ValueError('Raw JSON value can only be string or dict')
            # Handle both the output of calling /inventory/instances/...
            # and the _raw_data field value saved in our FolioRecord objects.
            if 'instances' in json_dict:
                json_dict = json_dict['instances'][0]
        else:
            request_url = url_template.format(self.okapi_url, identifier)
            json_dict = self._result_from_api(request_url, response_handler)
        if not json_dict:
            raise NotFound(f'Could not find a record for {identifier}')

        isbn_issn = isbn_issn_from_identifiers(json_dict['identifiers'])
        instance_id = json_dict['id']
        accession_number = self.accession_number_from_id(instance_id)
        title, author = parsed_title_and_author(json_dict['title'])
        if not author:
            author = pub_authors(json_dict['contributors'])
        rec = FolioRecord(id               = instance_id,
                          accession_number = accession_number,
                          isbn_issn        = isbn_issn,
                          title            = title,
                          author           = author,
                          year             = pub_year(json_dict['publication']),
                          publisher        = publisher(json_dict['publication']),
                          edition          = pub_edition(json_dict['editions']),
                          _raw_data        = json_dict)
        log(f'created {rec}')
        return rec


    def _result_from_api(self, url, result_producer, retry = 0):
        '''Do HTTP GET on "url" & return results of calling result_producer on it.'''
        headers = {
            "x-okapi-token": self.okapi_token,
            "x-okapi-tenant": self.tenant_id,
            "content-type": "application/json",
        }

        (resp, error) = net('get', url, headers = headers)
        if not error:
            if __debug__: log(f'got result from {url}')
            return result_producer(resp)
        elif isinstance(error, NoContent):
            if __debug__: log(f'got empty content from {url}')
            return result_producer(None)
        elif isinstance(error, RateLimitExceeded):
            retry += 1
            if retry > _MAX_SLEEP_CYCLES:
                raise FolioError(f'Rate limit exceeded for {url}')
            else:
                # Wait and then call ourselves recursively.
                if __debug__: log(f'hit rate limit; pausing {_RATE_LIMIT_SLEEP}s')
                wait(_RATE_LIMIT_SLEEP)
                return self._result_from_api(url, result_producer, retry = retry)
        elif isinstance(error, AuthenticationFailure):
            raise FolioPermissionError(f'Authentication error for {url}')
        else:
            raise FolioError(f'Problem contacting {url}: {antiformat(error)}')


    def accession_number_from_id(self, instance_id):
        if self.an_prefix.endswith('.'):
            prefix = self.an_prefix
        else:
            prefix = self.an_prefix + '.'
        return prefix + instance_id.replace('-', '.')


# Miscellaneous helpers.
# .............................................................................

def cleaned(text):
    '''Mildly clean up the given text string.'''
    if not text:
        return text
    text = text.rstrip('./')
    return text.strip()


def pub_year(publication_list):
    '''Return the publication year of the first entry in the publication list.'''
    if publication_list:
        year = publication_list[0]['dateOfPublication']
        return ''.join(filter(str.isdigit, year))
    else:
        return ''


def publisher(publication_list):
    '''Return the publisher name of the first entry in the publication list.'''
    if publication_list:
        return publication_list[0]['publisher']
    else:
        return ''


# Currently not used.
def pub_title(title_string):
    title, author = parsed_title_and_author(title_string)
    return cleaned(title)


def pub_authors(contributors):
    def extracted_name(field):
        author = field['name']
        # The names have additional trailing stuff that we want to remove.
        matched = regex.match(r'[-.,\p{L} ]+', author)
        if matched:
            return matched.group().strip(' ,')
        else:
            return author

    # Handle special case of et al.
    if len(contributors) == 1 and not contributors[0]['primary']:
        return extracted_name(contributors[0]) + ' et al.'
    return ' and '.join(extracted_name(author) for author in contributors)


def pub_edition(editions):
    if editions:
        return editions[0]
    return ''


def isbn_issn_from_identifiers(id_list):
    value_string = ''
    for entry in id_list:
        if entry['identifierTypeId'] in [_TYPE_ID_ISBN, _TYPE_ID_ISSN]:
            value_string = entry['value']
            break
    # Some have text after the isbn like '9780271067544 (pbk. : alk. paper)'.
    if ' ' in value_string:
        end = value_string.find(' ')
        return value_string[:end]
    elif value_string:
        return value_string
    else:
        return None


def id_from_an(accession_number):
    start = accession_number.find('.')
    id_part = accession_number[start + 1:]
    return id_part.replace('.', '-')


def parsed_title_and_author(text):
    '''Extract a title and authors (if present) from the given text string.'''
    title = None
    author = None
    if text.find('/ by') > 0:
        start = text.find('/ by')
        title = text[:start].strip()
        author = text[start + 4:].strip()
    elif text.find('[by]') > 0:
        start = text.find('[by]')
        title = text[:start].strip()
        author = text[start + 5:].strip()
    elif text.rfind(', by') > 0:
        start = text.rfind(', by')
        title = text[:start].strip()
        author = text[start + 5:].strip()
    elif text.find('/') > 0:
        start = text.find('/')
        title = text[:start].strip()
        author = text[start + 2:].strip()
    else:
        title = text
    if title.endswith(':'):
        title = title[:-1].strip()
    if author and author.startswith('edited by'):
        start = author.find('edited by')
        author = author[start + 9:].strip()
    if author and author.startswith('by'):   # In case nothing else catches it.
        start = author.find('by')
        author = author[start + 2:].strip()
    return cleaned(title), cleaned(author)
