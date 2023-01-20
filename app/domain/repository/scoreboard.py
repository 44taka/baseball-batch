from abc import ABC, abstractmethod

from domain.model.scoreboard import ScoreboardModel


class IScoreboardRepository(ABC):
    @abstractmethod
    def find(self, data: ScoreboardModel) -> ScoreboardModel:
        raise NotImplementedError

    @abstractmethod
    def insert(self, data: ScoreboardModel) -> ScoreboardModel:
        raise NotImplementedError

    @abstractmethod
    def update(self, data: ScoreboardModel) -> ScoreboardModel:
        raise NotImplementedError
