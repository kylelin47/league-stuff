import json
import os
import unittest

from pyriot.match import MatchHistoryAccessor
import pyriot.match as match

api_key = os.environ['RIOT_API_KEY']

class TestMatchHistory(unittest.TestCase):
    def setUp(self):
        self.mha = MatchHistoryAccessor(api_key, 'na')
        self.player_name = 'efdf'
        script_dir = os.path.dirname(__file__)
        rel_path = 'resources/history_data.json'
        self.abs_file_path = os.path.join(script_dir, rel_path)

    def test_first_blood_contributions(self):
        with open(self.abs_file_path) as data_file:
            history = json.load(data_file)
        self.assertEqual(match.get_first_blood_contributions(history), 1,
                         msg='Incorrect number of first blood contributions')

    def test_matches_filtered_by_region(self):
        na_matches = self.mha.get_match_history(self.player_name)
        self.mha.region = 'euw'
        euw_matches = self.mha.get_match_history(self.player_name)
        self.assertNotEqual(
            na_matches, euw_matches, msg='Different regions had same matches')

    def test_player_found_with_special_names(self):
        self.mha.region = 'euw'
        self.player_name = 'íNféKt'
        self.assertIsNotNone(
            self.mha.get_match_history(self.player_name),
            msg='Failed to retrieve matches from special name')

    def test_player_matches_retrieved(self):
        self.assertIsNotNone(
            self.mha.get_match_history(self.player_name),
            msg='Failed to retrieve any match history data')

    def test_number_of_matches(self):
        with open(self.abs_file_path) as data_file:
            history = json.load(data_file)
        self.assertEqual(match.get_number_of_matches(history), 10,
                         msg='Incorrect number of matches')

if __name__ == '__main__':
    unittest.main()
