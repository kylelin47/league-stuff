import os

from flask import Blueprint
from flask import render_template

import pyleague.match as match
import pyleagueweb.cache as cache

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
    expected_template = 'player.html'
    template_name = get_template_name(history, expected_template)
    if template_name is not expected_template:
        return render_template(template_name)

    p = Player(name=name,
               matches=match.get_number_of_matches(history),
               contributions=match.get_first_blood_contributions(history)
               )
    return render_template(expected_template,
                           player=p)


def get_match_history(region, name):
    cache_key = cache.generate_cache_key(region, name)
    history = cache.history_cache.get(cache_key)
    if history is None:
        mha = match.MatchHistoryAccessor(api_key, region)
        player_id = cache.id_cache.get(cache_key)
        try:
            if player_id is None:
                player_id = mha.get_id(name)
            history = mha.get_match_history(name, player_id=player_id)
        except TypeError:
            return None
        cache.id_cache.set(cache_key, player_id)
        cache.history_cache.set(cache_key, history)
    return history


def get_template_name(history, default):
    if history is None:
        return 'servers_unavailable.html'
    if 'matches' not in history:
        return 'no_match_history.html'
    return default
