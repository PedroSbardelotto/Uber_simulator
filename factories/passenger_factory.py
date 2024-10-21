from factories.abstract_factory import AbstractFactory
from models.passenger import Passageiro

class PassengerFactoryes(AbstractFactory):
    def criar_passageiro(self, nome, local_partida, destino):
        return Passageiro(nome,local_partida, destino)
    
    def criar_motorista(self,nome, veiculo):
        raise NotImplementedError("PassengerFactoryes não cria motorista.")
    