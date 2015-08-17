from flask import Blueprint
from flask import render_template

import pyleague.match as match
import pyleagueweb.cache as cache

player_api = Blueprint('player_api', __name__)


class Player:
    def __init__(self, name, matches, contributions):
        self.name = name
        self.matches = matches
        self.contributions = contributions


@player_api.route('/<region>/<name>/')
def show_player(region, name):
    history = cache.get_history(region, name)
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
    return render_template('player.html', player=p)
