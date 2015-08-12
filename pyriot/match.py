from .accessor import ApiAccessor

class MatchHistoryAccessor(ApiAccessor):
    def get_match_history(self, player_name):
        return self.get_json(
            self._address + '/v2.2/matchhistory/{}'.format(
                self.get_id(player_name)))
