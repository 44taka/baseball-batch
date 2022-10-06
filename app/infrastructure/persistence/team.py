from typing import List

from loguru import logger
from orator import DatabaseManager

from domain.model.team import TeamModel
from domain.repository.team import ITeamRepository


class TeamPersistence(ITeamRepository):

    def __init__(self, db: DatabaseManager):
        self._db = db

    def find_all(self) -> List[TeamModel]:
        # TODO: エラー処理を忘れずに
        result = self._db.table('team_mst').where('is_deleted', 0).get()
        return list(map(TeamModel.parse_obj, result))

    def find_by_id(self, team_id: int) -> TeamModel:
        # TODO: エラー処理を忘れずに
        query = self._db.table('team_mst')
        result = query.where('id', team_id).where('is_deleted', 0).get()
        return TeamModel.parse_obj(result)
