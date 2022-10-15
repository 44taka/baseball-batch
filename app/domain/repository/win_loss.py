from abc import ABC, abstractmethod
from typing import List
import datetime

from domain.model.win_loss import WinLossModel
from domain.model.win_loss_deposit import WinLossDepositModel


class IWinLossRepository(ABC):
    @abstractmethod
    def save(self, data: WinLossModel) -> WinLossModel:
        raise NotImplementedError

    @abstractmethod
    def calculate_deposit(self, date: datetime.date) -> List[WinLossDepositModel]:
        raise NotImplementedError
