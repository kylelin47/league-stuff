from logging.config import fileConfig

from flask import Flask
from flask import render_template
from flask import request

import cache
from fb import fb_api

app = Flask(__name__)

app.register_blueprint(fb_api)


@app.route('/')
def search_player():
    return render_template('index.html', regions=['NA', 'EUW', 'EUNE'],
                           name=request.args.get('name', 'N/A'))


@app.route('/playground/', methods=['POST'])
def view_cached_player_id():
    return str(
        cache.id_cache.get(cache.generate_cache_key(request.form['region'],
                                                    request.form['player'])))


if __name__ == '__main__':
    fileConfig('logging.conf')
    app.run(debug=True)
