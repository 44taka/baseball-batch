from abc import ABC, abstractmethod
from typing import List

from domain.model.team import TeamModel
from domain.model.scoreboard import ScoreboardModel


class IScrapingRepository(ABC):
    @abstractmethod
    def scrape(self, team_id: int, teams: List[TeamModel], url: str) -> List[ScoreboardModel]:
        raise NotImplementedError
