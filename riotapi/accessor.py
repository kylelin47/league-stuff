import requests

class ApiAccessor:

    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key
        self._payload = {'api_key' : api_key}

    def get_id(self, player_name):
        request_url = ('https://na.api.pvp.net/api/lol/na/v1.4/summoner'
                       '/by-name/{}'.format(player_name))
        return self.get_json(request_url)[player_name]['id']

    def get_json(self, url):
        return requests.get(url, params=self._payload).json()
