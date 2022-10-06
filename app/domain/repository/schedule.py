from abc import ABC, abstractmethod
from typing import List

from domain.model.schedule import ScheduleModel


class IScheduleRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[ScheduleModel]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, schedule_id: int) -> ScheduleModel:
        raise NotImplementedError
