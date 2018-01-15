# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# MIT License <https://opensource.org/licenses/MIT>

import json

from ._common import (BaseSource,)
from ..result import (AnicodeResult,)

import bs4
import requests


class UnicodeTableSource(BaseSource):
    """ The source handler for unicode-table.com.
    """

    _source_url = 'https://unicode-table.com/en/a-s/'

    def search(self, query, callback, count=10):
        """ Sends query results over a callback.

        .. note:: The callback should accept the following positional
            parameters:

            * The query source object
            * The AnicodeResult object

        :param str query: The search term to use
        :param callable callback: The callback function
        :param int count: The number of results to send to the callback
        :returns: Does not return
        """

        results = {}
        response = requests.post(
            self._source_url,
            data={'p': query, 'o': 0, 'l': count}
        )
        if response.status_code == 200:
            results = json.loads(response.text).get('result', {})
            if results and (len(results.get('h', '')) > 0):
                soup = bs4.BeautifulSoup(results.get('h'), 'lxml')
                for character in soup.find_all('li', {'class': 'clearfix'}):
                    character_href = character.find('a')
                    callback(self, AnicodeResult(
                        character_href.text,
                        int(character_href.attrs[
                            'href'
                        ].rstrip('/').split('/')[-1], 16)
                    ))
