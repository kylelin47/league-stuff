import os
import unittest

from riotapi.match import MatchHistoryRetriever

api_key = os.environ['RIOT_API_KEY']

class TestMatchHistoryRetriever(unittest.TestCase):

    def setUp(self):
        self.mhr = MatchHistoryRetriever(api_key)

    def test_data_is_retrieved(self):
        self.assertIsNotNone(self.mhr.get_match_history('efdf')['matches'])

if __name__ == '__main__':
    unittest.main()
