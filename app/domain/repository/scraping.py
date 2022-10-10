from abc import ABC, abstractmethod
from typing import List

from domain.model.win_loss import WinLossModel


class IScrapingRepository(ABC):
    @abstractmethod
    def scrape(self, team_id: int, url: str) -> List[WinLossModel]:
        raise NotImplementedError
