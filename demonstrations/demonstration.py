import json
import os

from riotapi.match import MatchHistoryRetriever

if __name__ == '__main__':
    api_key = os.environ['RIOT_API_KEY']
    mhr = MatchHistoryRetriever(api_key)
    print(json.dumps(mhr.get_match_history('efdf'), sort_keys=True, indent=4))
