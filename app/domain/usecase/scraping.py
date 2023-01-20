from abc import ABC, abstractmethod
from typing import List

from domain.model.team import TeamModel


class IScrapingUseCase(ABC):
    @abstractmethod
    def scrape(self, team_id: int, teams: List[TeamModel], url: str) -> int:
        raise NotImplementedError
