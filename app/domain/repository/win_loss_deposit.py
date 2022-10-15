from abc import ABC, abstractmethod

from domain.model.win_loss_deposit import WinLossDepositModel


class IWinLossDepositRepository(ABC):

    @abstractmethod
    def save(self, data: WinLossDepositModel) -> WinLossDepositModel:
        raise NotImplementedError
