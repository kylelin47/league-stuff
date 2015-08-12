import json
import os

from pyriot.match import MatchHistoryAccessor

if __name__ == '__main__':
    api_key = os.environ['RIOT_API_KEY']
    mha = MatchHistoryAccessor(api_key, 'na')
    print(json.dumps(mha.get_match_history('efdf'), sort_keys=True, indent=4))
