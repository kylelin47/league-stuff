import json
import os
import requests

api_key = os.environ['RIOT_API_KEY']
key_url = '?api_key={}'.format(api_key)

def get_id(player_name):
    request_url = ('https://na.api.pvp.net/api/lol/na/v1.4/summoner'
                   '/by-name/{}{}'.format(player_name, key_url))
    return get_json(request_url)[player_name]['id']

def get_json(url):
    return requests.get(url).json()

def get_match_history(player_name):
    return get_json(
        'https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/{}{}'.format(
        get_id(player_name), key_url))

if __name__ == '__main__':
    print(get_match_history('efdf'))
