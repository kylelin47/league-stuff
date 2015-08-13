import os

from flask import Flask
from flask import render_template
from flask import request
from werkzeug.contrib.cache import SimpleCache

import pyriot.match as match

app = Flask(__name__)
id_cache = SimpleCache(default_timeout=60 * 60 * 24 * 7)
history_cache = SimpleCache()

api_key = os.environ['RIOT_API_KEY']


@app.route('/')
def search_player():
    return render_template('index.html', regions=['NA', 'EUW', 'EUNE'],
                           name=request.args.get('name', 'N/A'))


@app.route('/<region>/<name>')
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


def generate_cache_key(region, name):
    return region.upper() + ''.join(name.lower().split())


def get_match_history(region, name):
    cache_key = generate_cache_key(region, name)
    history = history_cache.get(cache_key)
    if history is None:
        mha = match.MatchHistoryAccessor(api_key, region)
        player_id = id_cache.get(cache_key)
        try:
            if player_id is None:
                player_id = mha.get_id(name)
            history = mha.get_match_history(name, player_id=player_id)
        except TypeError:
            return None
        id_cache.set(cache_key, player_id)
        history_cache.set(cache_key, history)
    return history


def get_template_name(history, default):
    if history is None:
        return 'servers_unavailable.html'
    if 'matches' not in history:
        return 'no_match_history.html'
    return default


if __name__ == '__main__':
    app.run(debug=True)
