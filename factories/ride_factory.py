from abc import ABC, abstractmethod
class Ridefactory(ABC):
    @abstractmethod
    def criar_corrida(self, driver, passenger, distance):
        pass
