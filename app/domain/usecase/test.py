from abc import ABC, abstractmethod


class ITestUseCase(ABC):
    @abstractmethod
    def find_all(self):
        raise NotImplementedError
