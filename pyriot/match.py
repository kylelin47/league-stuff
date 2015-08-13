from .accessor import ApiAccessor


class MatchHistoryAccessor(ApiAccessor):
    def get_match_history(self, player_name, player_id=None):
        if player_id is None:
            player_id = self.get_id(player_name)
        return self.get_json(
            self._address + '/v2.2/matchhistory/{}'.format(player_id))


def get_first_blood_contributions(match_history):
    contributions = 0
    for match in match_history['matches']:
        assert len(match['participants']) == 1
        match_stats = match['participants'][0]['stats']
        if match_stats['firstBloodKill'] or match_stats['firstBloodAssist']:
            contributions += 1
    return contributions


def get_number_of_matches(match_history):
    return len(match_history['matches'])
