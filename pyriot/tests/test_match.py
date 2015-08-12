import os
import unittest

from pyriot.match import MatchHistoryAccessor

api_key = os.environ['RIOT_API_KEY']

class TestMatchHistoryRetriever(unittest.TestCase):
    def setUp(self):
        self.mha = MatchHistoryAccessor(api_key, 'na')
        self.player_name = 'efdf'

    def test_player_matches_retrieved(self):
        self.assertIsNotNone(
            self.mha.get_match_history(self.player_name)['matches'])

if __name__ == '__main__':
    unittest.main()
