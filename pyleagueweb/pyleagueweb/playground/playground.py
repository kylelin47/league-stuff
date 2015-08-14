from flask import Blueprint
from flask import render_template
from flask import request

import pyleagueweb.cache as cache

playground = Blueprint('playground', __name__)


@playground.route('/')
def search_player():
    return render_template('index.html', regions=['NA', 'EUW', 'EUNE'],
                           name=request.args.get('name', 'N/A'))


@playground.route('/playground/', methods=['POST'])
def view_cached_player_id():
    return str(
        cache.id_cache.get(cache.generate_cache_key(request.form['region'],
                                                    request.form['player'])))
