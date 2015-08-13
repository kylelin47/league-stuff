import os

from flask import Flask
from flask import render_template

import pyriot.match as match

app = Flask(__name__)
api_key = os.environ['RIOT_API_KEY']

@app.route('/')
def search_player():
    return render_template('index.html')

@app.route('/<name>')
def show_fb(name):
    mha = match.MatchHistoryAccessor(api_key, 'na')
    history = mha.get_match_history(name)
    return 'contribution percent: {:.2%}'.format(
        match.get_first_blood_contributions(
            history) / match.get_number_of_matches(history))

if __name__ == '__main__':
    app.run(debug=True)
