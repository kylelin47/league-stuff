from .accessor import ApiAccessor

class MatchHistoryRetriever(ApiAccessor):

    def get_match_history(self, player_name):
        return self.get_json(
            'https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/{}'.format(
                self.get_id(player_name)))
