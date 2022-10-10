from abc import ABC, abstractmethod


class IScrapingUseCase(ABC):
    @abstractmethod
    def scrape(self, url: str) -> int:
        raise NotImplementedError
