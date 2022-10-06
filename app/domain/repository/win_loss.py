from abc import ABC, abstractmethod

from domain.model.win_loss import WinLossModel


class IWinLossRepository(ABC):
    @abstractmethod
    def save(self, data: WinLossModel) -> WinLossModel:
        raise NotImplementedError
