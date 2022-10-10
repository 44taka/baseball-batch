from typing import List

from orator import DatabaseManager
from loguru import logger

from domain.model.team import TeamModel
from domain.repository.team import ITeamRepository


class TeamPersistence(ITeamRepository):

    def __init__(self, db: DatabaseManager):
        self._db = db

    def find_all(self) -> List[TeamModel]:
        try:
            result = self._db.table('team_mst').where('is_deleted', 0).get()
            return list(map(TeamModel.parse_obj, result))
        except Exception as e:
            logger.exception(e)
            raise

    def find_by_id(self, team_id: int) -> TeamModel:
        try:
            query = self._db.table('team_mst')
            result = query.where('id', team_id).where('is_deleted', 0).first()
            if result is None:
                raise Exception('team is not found.')
            return TeamModel.parse_obj(result)
        except Exception as e:
            logger.exception(e)
            raise
