from abc import ABC, abstractmethod


class IScrapingUseCase(ABC):
    @abstractmethod
    def scrape(self, team_id: int, url: str) -> int:
        raise NotImplementedError
