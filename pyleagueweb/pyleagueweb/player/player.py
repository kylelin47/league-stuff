import logging
import os

from flask import Blueprint
from flask import render_template

import pyleague.exceptions
import pyleague.match as match
import pyleagueweb.cache as cache

logger = logging.getLogger(__name__)
player_api = Blueprint('player_api', __name__)

api_key = os.environ['RIOT_API_KEY']


class Player:
    def __init__(self, name, matches, contributions):
        self.name = name
        self.matches = matches
        self.contributions = contributions


@player_api.route('/<region>/<name>/')
def show_player(region, name):
    history = get_match_history(region, name)
    if history is None:
        return render_template('errors/other.html',
                               error='data unavailable. make sure this guy '
                                     'exists and try again later')
    if history == {}:
        return render_template('errors/other.html',
                               error='riot\'s error codes are bad. this guy '
                                     'exists but has no history')
    p = Player(name=name,
               matches=match.get_number_of_matches(history),
               contributions=match.get_first_blood_contributions(history)
               )
    return render_template('player.html',
                           player=p)


def get_match_history(region, name):
    cache_key = cache.generate_cache_key(region, name)
    history = cache.history_cache.get(cache_key)
    if history == cache.null_value:
        return None
    if history is None:
        mha = match.MatchHistoryAccessor(api_key, region)
        player_id = cache.id_cache.get(cache_key)
        if player_id == cache.null_value:
            return None
        try:
            if player_id is None:
                player_id = mha.get_id(name)
            history = mha.get_match_history(player_id=player_id)
        except pyleague.exceptions.PyLeagueError as e:
            logger.warning(e)
            if '404' in str(e):
                player_id = cache.null_value
                history = cache.null_value
            return None
        finally:
            cache.id_cache.set(cache_key, player_id)
            cache.history_cache.set(cache_key, history)
    return history
