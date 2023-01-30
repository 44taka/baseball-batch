from abc import ABC, abstractmethod


class INpbUseCase(ABC):
    @abstractmethod
    def register(self, team_id: int, url: str) -> None:
        raise NotImplementedError
