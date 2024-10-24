from abc import ABC, abstractmethod
from models.driver import Motorista
from models.passenger import Passageiro 

class abstractFactory(ABC):
    @abstractmethod
    def criar_motorista(self, nome, veiculo):
        pass

    @abstractmethod
    def criar_passageiro(self, nome, local_partida, destino):
        pass

    @abstractmethod
    def criar_corrida(self, driver, passenger, distance):
        pass