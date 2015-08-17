import logging
import os

from werkzeug.contrib.cache import SimpleCache

import pyleague.accessor as accessor
import pyleague.exceptions
import pyleague.match as match

logger = logging.getLogger(__name__)

id_cache = SimpleCache(default_timeout=60 * 60 * 24 * 7)
history_cache = SimpleCache()
null_value = 'N/A'

api_key = os.environ['RIOT_API_KEY']


def generate_cache_key(region, name):
    return region.upper() + ''.join(name.lower().split())


def get_id(region, name):
    cache_key = generate_cache_key(region, name)
    player_id = id_cache.get(cache_key)
    if player_id == null_value:
        return None
    if player_id is None:
        api = accessor.ApiAccessor(api_key, region)
        try:
            player_id = api.get_id(name)
        except pyleague.exceptions.PyLeagueError as e:
            logger.warning(e)
            if '404' in str(e):
                player_id = null_value
            return None
        finally:
            id_cache.set(cache_key, player_id)
    return player_id


def get_history(region, name):
    cache_key = generate_cache_key(region, name)
    history = history_cache.get(cache_key)
    if history == null_value:
        return None
    if history is None:
        mha = match.MatchHistoryAccessor(api_key, region)
        player_id = get_id(region, name)
        try:
            history = mha.get_match_history(player_id=player_id)
        except TypeError:
            return None
        except pyleague.exceptions.PyLeagueError as e:
            logger.warning(e)
            if '404' in str(e):
                history = null_value
            return None
        finally:
            history_cache.set(cache_key, history)
    return history
