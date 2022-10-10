from orator import DatabaseManager
from loguru import logger

from domain.model.win_loss import WinLossModel
from domain.repository.win_loss import IWinLossRepository


class WinLossPersistence(IWinLossRepository):

    def __init__(self, db: DatabaseManager):
        self._db = db

    def save(self, data: WinLossModel) -> WinLossModel:
        try:
            query = self._db.table('win_loss_tbl')
            if data.id is None:
                # insert処理
                result = query.insert_get_id(data.dict())
                if result > 0:
                    data.id = result
                return data
            else:
                # update処理
                query.where('id', data.id).update(data.dict())
            return data
        except Exception as e:
            logger.exception(e)
            raise
