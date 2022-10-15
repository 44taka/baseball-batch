from abc import ABC, abstractmethod
import datetime


class IAggregatingUseCase(ABC):
    @abstractmethod
    def aggregate(self, date: datetime.date) -> int:
        raise NotImplementedError
