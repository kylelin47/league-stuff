import os
import unittest

from pyriot.match import MatchHistoryAccessor

api_key = os.environ['RIOT_API_KEY']

class TestMatchHistoryAccessor(unittest.TestCase):
    def setUp(self):
        self.mha = MatchHistoryAccessor(api_key, 'na')
        self.player_name = 'efdf'

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
            self.mha.get_match_history(self.player_name)['matches'],
            msg=('Failed to retrieve matches from special name'))

    def test_player_matches_retrieved(self):
        self.assertIsNotNone(
            self.mha.get_match_history(self.player_name)['matches'],
            msg='Failed to retrieve any match history data')

if __name__ == '__main__':
    unittest.main()
