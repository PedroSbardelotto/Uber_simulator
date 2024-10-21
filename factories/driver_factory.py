from models.driver import Motorista
from factories.abstract_factory import AbstractFactory


class DrivenFactory(AbstractFactory):
    def criar_motorista(self, nome, veiculo):
        return
    
    def criar_passageiros(self, nome, local_paetida, destino):
        raise NotImplementedError("DrivenFactory não cria passageiros.")
    
