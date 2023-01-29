from abc import ABC, abstractmethod
from typing import List, Union

from domain.model.team import TeamModel


class ITeamRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[TeamModel]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, team_id: int) -> Union[TeamModel, None]:
        raise NotImplementedError
