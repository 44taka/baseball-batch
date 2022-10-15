import datetime

from loguru import logger

from domain.repository.win_loss import IWinLossRepository
from domain.repository.win_loss_deposit import IWinLossDepositRepository
from domain.usecase.aggregating import IAggregatingUseCase


class AggregatingUseCase(IAggregatingUseCase):

    def __init__(self, wlr: IWinLossRepository, wldr: IWinLossDepositRepository):
        self._wlr = wlr
        self._wldr = wldr

    def aggregate(self, date: datetime.date) -> int:
        try:
            result = self._wlr.calculate_deposit(date)
            for datum in result:
                self._wldr.save(data=datum)
            return 0
        except Exception as e:
            raise e
