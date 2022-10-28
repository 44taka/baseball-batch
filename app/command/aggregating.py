import sys

from loguru import logger
from datetime import date

from utils.util import Util
from configs.database import db
from infrastructure.persistence.win_loss import WinLossPersistence
from infrastructure.persistence.win_loss_deposit import WinLossDepositPersistence
from usecase.aggregating import AggregatingUseCase
from presentation.aggregating import AggregatingPresentation


class AggregatingCommand(object):

    def run(self) -> None:
        logger.info('start aggregation command.')

        # 処理準備
        win_loss_persistence = WinLossPersistence(db=db)
        win_loss_deposit_persistence = WinLossDepositPersistence(db=db)
        aggregating_usecase = AggregatingUseCase(
            wlr=win_loss_persistence, wldr=win_loss_deposit_persistence
        )
        aggregating_presentation = AggregatingPresentation(agu=aggregating_usecase)

        # 処理開始
        status = 0
        for day in Util.get_date_list(begin_date=date(2022, 3, 25), end_date=date(2022, 10, 3)):
            status = aggregating_presentation.run(date=day)
            if status > 0:
                break
        logger.info('end aggregation command.')
        sys.exit(status)
