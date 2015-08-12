import os
import unittest

from pyriot.match import MatchHistoryAccessor

api_key = os.environ['RIOT_API_KEY']

class TestMatchHistoryRetriever(unittest.TestCase):
    def setUp(self):
        self.mha = MatchHistoryAccessor(api_key, 'na')

    def test_data_is_retrieved(self):
        self.assertIsNotNone(self.mha.get_match_history('efdf')['matches'])


if __name__ == '__main__':
    unittest.main()
