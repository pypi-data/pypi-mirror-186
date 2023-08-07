from datetime import datetime
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from collections import OrderedDict
from libms.infodict import InfoDict
import weakref
import re
import json
import time
import logging
import ssl

class NZBError(Exception):
    pass

class NZB(object):
    """
    Encapsulate an NZB
    """
    DATE_STRIP_RE = re.compile(r'^.*?, (\d+ \w+ \d+ [\d:]+) [-\+]\d+')
    SIZE_MAP = (
        (1024 ** 3, 'G'),
        (1024 ** 2, 'M'),
        (1024, 'K'),
        (0, 'B'),
    )

    def __init__(self, newznab, guid=None, search_dict=None):
        """
        Create an nzb object using a given guid or search_dict.  One of
        the 2 must be specified.

        newznab:Newznab     A Newznab object
        guid:str            The guid for an nzb.  This will be used to look
                            up metadata
        search_dict:dict    The dictionary of nzb metadata from a search
        """
        self.newznab = weakref.proxy(newznab)
        self.guid = guid
        self._search_dict = search_dict
        if not guid and not search_dict:
            raise NZBError('A guid or search_dict must be supplied when '
                'creating an NZB object')
        self.size = None
        self.description = None
        self.title = None
        self.pub_date = None
        self.download_url = None
        self.category = None
        self.cat_ids = []

        if self.guid:
            self._process_guid()
        else:
            self._process_sd()

    def __str__(self):
        return self.download_url

    def __repr__(self):
        return self.download_url

    def get_size_str(self):
        for min_size, letter in self.SIZE_MAP:
            if self.size > min_size:
                return '{:.2f}{}'.format(self.size / float(min_size), letter)

        raise NZBError('Unknown size conversion for size: {}'.format(self.size))

    def _process_guid(self):
        url = '{}{}'.format(
            self.newznab.url_base,
            urlencode({
                't': 'details',
                'id': self.guid,
                'apikey': self.newznab.api_key,
                'o': 'json',
            }),
        )

        res = Newznab.open_url(url)
        details = json.loads(res.read().decode('utf-8', errors='ignore'))
        self._process_details(details)

    def _process_details(self, details):
        if isinstance(details, (list, tuple)):
            self._handle_item_dict(details[0])
        else:
            item = details['channel']['item']
            self._handle_item_dict(item)

    def _process_sd(self):
        self._handle_item_dict(self._search_dict)

    def _handle_attributes(self, attrs):
        for a in attrs:
            attr_name = a['@attributes']['name']
            attr_val = a['@attributes']['value']

            if attr_name == 'category':
                self.cat_ids.append(attr_val)
            elif attr_name == 'size':
                self.size = int(attr_val)
            elif attr_name == 'guid':
                self.guid = attr_val

    def _handle_item_dict(self, item):
        if 'attr' in item:
            self._handle_attributes(item['attr'])
            self.category = item['category']
        else:
            self.guid = item['id']
            self.category = item['category_name']
            self.size = int(item['size'])

        self.description = item.get('description', '')
        self.download_url = item['link'] if 'link' in item else \
            self._construct_item_link(item)
        self.title = item['title']
        pub_str = item['pubDate'] if 'pubDate' in item else item['pubdate']
        self.pub_date = self._process_pub_date(pub_str)

    def _process_pub_date(self, date_str):
        """
        Date str is in the form of: Thu, 30 Jun 2016 02:45:58 -0700
        """
        # Strip the day of the week and time zone info
        m = self.DATE_STRIP_RE.match(date_str)
        if not m:
            raise NZBError('Error parsing date: {}'.format(date_str))
        dstr = m.group(1)
        dt = datetime.strptime(dstr, '%d %b %Y %H:%M:%S')
        return dt

    def _construct_item_link(self, item):
        url = '{}/getnzb/{}.nzb&{}'.format(
            self.newznab._url_base,
            item['id'],
            urlencode({
                'i': self.newznab.i,
                'r': self.newznab.api_key,
            })
        )

        return url


class Newznab(object):
    def __init__(self, url_base, api_key, i=1, headers=None):
        """
        Sets up a newznab object

        url_base:str        The base url for the newznab server.  Should be
                            something like http[s]://www.example.com[:port]
        api_key:str         The newznab API key
        i:int               Some integer value that can be used for url
                            construction
        headers:dict[str,str]   An optional dict of headers to send to the
                                server
        """
        self._url_base = url_base
        self.url_base = '{}/api?'.format(url_base.rstrip('/'))
        self.api_key = api_key
        self.i = i
        self._search_cats = None
        self.headers = headers if headers else {}

    @property
    def search_cats(self):
        if self._search_cats is not None:
            return self._search_cats
        return self.get_search_cats()

    def get_nzb(self, guid):
        """
        Returns an nzb object for the given guid

        returns NZB
        """
        return NZB(self, guid)

    def get_nzb_from_search(self, search_dict):
        """
        Returns an nzb object for the given search result dictionary

        returns NZB
        """
        return NZB(self, search_dict=search_dict)

    @staticmethod
    def open_url(url, num_retries=5, headers=None):
        tries = 0
        last_exc = None
        res = None
        headers = headers if headers else {}
        req = Request(url, headers=headers)
        #ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
        #ctx.verify_mode = ssl.CERT_NONE
        #ctx.check_hostname = False
        while tries < num_retries:
            try:
                res = urlopen(req)
            except Exception as e:
                last_exc = e
                tries += 1
            else:
                return res
            time.sleep(tries ** 2)

        if res is None and last_exc is not None:
            raise last_exc
        else:
            return res

    def search(self, search, cat='movies', cat_num=None):
        """
        Returns a list of search results as NZB objects

        search:str      What you are searching for
        cat:str         The category to search within.  It must be one of
                        the SEARCH_CAT categories

        returns list[NZB]       Returns a list of nzbs
        """
        ret = []

        cat = cat.lower()
        if not cat_num:
            if cat not in self.search_cats:
                raise NZBError('Invalid search category: {}'.format(cat))
            cat_num = self.search_cats[cat]

        url = '{}{}'.format(
            self.url_base,
            urlencode({
                't': 'search',
                'apikey': self.api_key,
                'q': search,
                'o': 'json',
                'cat': cat_num,
            })
        )

        res = Newznab.open_url(url, headers=self.headers)
        logging.debug('Performing search via url: {}'.format(url))
        res_str = res.read()
        try:
            o = json.loads(res_str.decode('utf-8', errors='ignore'))
        except Exception:
            logging.debug('Could not process search for "{}" at {}: {}'.format(
                search, url, res_str))
            return ret

        if isinstance(o, (list, tuple)):
            # nzbs.today returns different data :/
            for i in o:
                ret.append(self.get_nzb_from_search(i))
        elif 'channel' in o and 'item' in o['channel']:
            if isinstance(o['channel']['item'], (list, tuple)):
                for i in o['channel']['item']:
                    ret.append(self.get_nzb_from_search(i))
            elif isinstance(o['channel']['item'], dict):
                ret.append(self.get_nzb_from_search(o['channel']['item']))

        return ret

    def get_most_recent(self, num_items=1, cat=None):
        """
        Returns "num_items" most recently added

        num_items:int   The number of recent items to return
        cat:str         The category to search within.  It must be one of
                        the SEARCH_CAT categories

        returns list[NZB]       Returns a list of nzbs
        """
        ret = []

        if cat is not None and cat.lower() not in SEARCH_CATS:
            raise NZBError('Invalid search category: {}'.format(cat))

        args = {
            't': 'search',
            'apikey': self.api_key,
            'o': 'json',
            'limit': num_items,
        }
        if cat:
            args['cat'] = cat

        url = '{}{}'.format(
            self.url_base,
            urlencode(args),
        )

        res = Newznab.open_url(url, headers=self.headers)
        o = json.loads(res.read().decode('utf-8'))

        if isinstance(o, (list, tuple)):
            for i in o:
                ret.append(self.get_nzb_from_search(i))
        elif 'item' in o['channel']:
            if isinstance(o['channel']['item'], (list, tuple)):
                for i in o['channel']['item']:
                    ret.append(self.get_nzb_from_search(i))
            elif isinstance(o['channel']['item'], dict):
                ret.append(self.get_nzb_from_search(o['channel']['item']))

        return ret

    def get_search_cats(self):
        """
        Get the map of top level search categories from the newznab server

        return dict<str, int>   The dictionary of category -> category id num
        """
        ret = OrderedDict()

        url = '{}{}'.format(
            self.url_base,
            urlencode({
                't': 'caps',
                'o': 'json',
            }),
        )

        res = Newznab.open_url(url, headers=self.headers)
        try:
            res_str = res.read().decode('utf-8', errors='ignore')
            if res_str.lower() == 'null':
                raise RuntimeError('Received "null"')
            o = json.loads(res_str)
        except Exception as e:
            logging.debug('Failed to load JSON for capabilities: '
                '{}'.format(e))
            # Need to try with xml
            url = '{}{}'.format(
                self.url_base,
                urlencode({
                    't': 'caps',
                }),
            )

            res = Newznab.open_url(url)
            data = res.read()
            o = None
            try:
                o = InfoDict.xml_to_info_dict(res.read())['caps']
            except Exception:
                print('FAILED to parse data from url {}: {}'.format(url, data))

        if not o:
            return ret

        for cat in o['categories']['category']:
            if '@attributes' in cat:
                attrs = cat['@attributes']
                ret[attrs['name'].lower()] = int(attrs['id'])
            else:
                ret[cat['name'].lower()] = int(cat['id'])

        self._search_cats = ret

        return ret
    # Alias
    get_categories = get_search_cats
