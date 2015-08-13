import requests


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
        request_url = self._address + '/v1.4/summoner/by-name/{}'.format(
            player_name)
        return self.get_json(request_url)[player_name.lower()]['id']

    def get_json(self, url):
        try:
            return requests.get(url, params=self._payload).json()
        except ValueError:
            return None
