import logging

import requests

from pyleague.versions import versions

logger = logging.getLogger(__name__)


class ApiAccessor:
    def __init__(self, api_key, region):
        self.api_key = api_key
        self.region = region

    @property
    def api_key(self):
        return self._api_key

    @property
    def region(self):
        return self._region

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key
        self._payload = {'api_key': api_key}

    @region.setter
    def region(self, region):
        self._region = region
        self._address = 'https://{0}.api.pvp.net/api/lol/{0}'.format(
            self.region)

    def get_id(self, player_name):
        logger.info('Getting id of player {}'.format(player_name))
        player_name = ''.join(player_name.split())
        data_type = 'summoner'
        request_url = (self._address +
                       '/{}/{}/by-name/{}'.format(versions[data_type],
                                                  data_type,
                                                  player_name))
        return self.get_json(request_url)[player_name.lower()]['id']

    def get_json(self, url):
        try:
            return requests.get(url, params=self._payload).json()
        except ValueError:
            return None
