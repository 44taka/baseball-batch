from orator import DatabaseManager
from loguru import logger
from typing import List
import datetime

from domain.model.win_loss import WinLossModel
from domain.model.win_loss_deposit import WinLossDepositModel
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

    def calculate_deposit(self, date: datetime.date) -> List[WinLossDepositModel]:
        try:
            result = self._db.table('win_loss_tbl') \
                .select(
                    'team_id',
                    self._db.raw(
                        '(sum(case is_win when 1 then 1 else 0 end) - '
                        'sum(case is_lose when 1 then 1 else 0 end)) as deposit'
                    ),
                    self._db.raw('\'' + str(date) + '\' as date')
                ) \
                .join('team_mst', 'win_loss_tbl.team_id', '=', 'team_mst.id') \
                .where('win_loss_tbl.is_deleted', 0) \
                .where('team_mst.is_deleted', 0) \
                .where_in('game_status', [1, 2]) \
                .where('date', '<=', date) \
                .group_by('team_id') \
                .get()
            return list(map(WinLossDepositModel.parse_obj, result))
        except Exception as e:
            logger.error(e)
            raise
