import json
import os
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

class MatchHistoryRetriever(ApiAccessor):

    def get_match_history(self, player_name):
        return self.get_json(
            'https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/{}'.format(
            self.get_id(player_name)))

if __name__ == '__main__':
    api_key = os.environ['RIOT_API_KEY']
    mhr = MatchHistoryRetriever(api_key)
    print(json.dumps(mhr.get_match_history('efdf'), sort_keys=True, indent=4))
