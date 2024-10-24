from factories.abstract_factory import abstractFactory
from models.passenger import Passageiro

class PassengerFactoryes(abstractFactory):
    def criar_passageiro(self, nome, destino):
        return Passageiro(nome, destino)
    
    def criar_motorista(self,nome, veiculo):
        raise NotImplementedError("PassengerFactoryes não cria motorista.")
    
    def criar_corrida(self, driver, passenger, distance):
        raise NotImplementedError("PassengerFactoryes não cria corridas.")