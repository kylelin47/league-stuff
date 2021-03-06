import logging

from pyleague.accessor import ApiAccessor
from pyleague.versions import versions

logger = logging.getLogger(__name__)


class MatchHistoryAccessor(ApiAccessor):
    def get_match_history(self, player_name=None, player_id=None):
        if player_name is None and player_id is None:
            raise TypeError('At least one identifier is required')
        if player_id is None:
            player_id = self.get_id(player_name)
        logger.info('Accessing player match history')
        data_type = 'matchhistory'
        payload = {'rankedQueues': 'RANKED_SOLO_5x5,RANKED_TEAM_5x5'}
        return self.get_json(
            self._address + '/{}/{}/{}'.format(versions[data_type], data_type,
                                               player_id), payload=payload)


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
