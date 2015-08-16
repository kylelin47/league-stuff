import os
from logging.config import fileConfig

from flask import Flask
from flask import render_template

from pyleagueweb.player.player import player_api
from pyleagueweb.playground.playground import playground

app = Flask(__name__)
# if two routes are identical it goes to the first one it finds top to bottom
# if two routes match it goes to the more specific one

app.register_blueprint(player_api, url_prefix='/players')
app.register_blueprint(playground)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    fileConfig(os.path.join(script_dir, 'logging.conf'))
    app.run(debug=True)
