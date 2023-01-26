from orator import DatabaseManager
from loguru import logger

from domain.model.scoreboard import ScoreboardModel
from domain.repository.scoreboard import IScoreboardRepository


class ScoreboardPersistence(IScoreboardRepository):

    def __init__(self, db: DatabaseManager):
        self._db = db

    def find(self, data: ScoreboardModel) -> ScoreboardModel:
        try:
            query = self._db.table('scoreboard_tbl') \
                .where('team_id', data.team_id) \
                .where('vs_team_id', data.vs_team_id) \
                .where('date', data.date) \
                .where('is_deleted', 0)
            # logger.debug(query.to_sql())
            return query.first()
        except Exception as e:
            logger.error(e)
            raise

    def insert(self, data: ScoreboardModel) -> ScoreboardModel:
        try:
            query = self._db.table('scoreboard_tbl')
            result = query.insert_get_id(data.dict())
            if result > 0:
                data.id = result
            return data
        except Exception as e:
            logger.error(e)
            raise

    def update(self, data: ScoreboardModel) -> ScoreboardModel:
        try:
            data_dict = data.dict()
            del data_dict['created_at'], data_dict['id']
            self._db.table('scoreboard_tbl') \
                .where('team_id', data.team_id) \
                .where('vs_team_id', data.vs_team_id) \
                .where('date', data.date) \
                .where('is_deleted', 0) \
                .update(data_dict)
            return data
        except Exception as e:
            logger.error(e)
            raise
