import os

from flask import Blueprint
from flask import render_template

import pyriot.match as match
import cache

fb_api = Blueprint('fb_api', __name__)

api_key = os.environ['RIOT_API_KEY']


@fb_api.route('/<region>/<name>/')
def show_fb(region, name):
    history = get_match_history(region, name)
    expected_template = 'first_blood.html'
    template_name = get_template_name(history, expected_template)
    if template_name is not expected_template:
        return render_template(template_name)
    return render_template(expected_template,
                           contributions=match.get_first_blood_contributions(
                               history),
                           matches=match.get_number_of_matches(history),
                           name=name)


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
