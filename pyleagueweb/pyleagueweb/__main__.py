import os
from logging.config import fileConfig

from flask import Flask

from pyleagueweb.player.player import player_api
from pyleagueweb.playground.playground import playground

app = Flask(__name__)

app.register_blueprint(player_api, url_prefix='/players')
app.register_blueprint(playground)

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    fileConfig(os.path.join(script_dir, 'logging.conf'))
    app.run(debug=True)
