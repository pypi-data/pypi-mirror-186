from urllib.parse import urlencode
from urllib.request import urlopen
import json

class Sabnzbd(object):
    def __init__(self, url_base, api_key):
        """
        Set up an sabnzbd api object.

        url_base:str        The base url.  Should be of the form:
                            http[s]://www.example.com[:port]
        api_key:str         The api key for sabnzbd
        """
        self.url_base = '{}/api?'.format(url_base.rstrip('/'))
        self.api_key = api_key
        self._cats = None

    @property
    def cats(self):
        if self._cats is None:
            self._cats = self.get_categories()
        return self._cats

    def get_categories(self):
        """
        Get a list of category names from SAB

        returns list[str]   The list of API categories
        """
        url = '{}{}'.format(
            self.url_base,
            urlencode({
                'mode': 'get_cats',
                'apikey': self.api_key,
                'output': 'JSON',
            }),
        )

        res = urlopen(url)

        # The sab clowns ship it with single quotes instead of valid json
        fixed = res.read().decode('utf-8').replace("'", '"')

        return json.loads(fixed)

    def get_add_nzb_url(self, nzb, cat='movies'):
        """
        Get the url to add an nzb via the API

        nzb:NZB         This is an nzb object that includes the newznab info
        cat:str         The sabnzbd category to set

        returns str     Returns the full "add to sabnzbd" url
        """
        url = '{}{}'.format(
            self.url_base,
            urlencode({
                'mode': 'addurl',
                'name': nzb.download_url,
                'apikey': self.api_key,
                'cat': cat,
            }),
        )

        return url

