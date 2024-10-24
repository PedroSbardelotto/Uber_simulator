from models.driver import Motorista
from factories.abstract_factory import abstractFactory


class DriverFactory(abstractFactory):
    def criar_motorista(self, nome, veiculo, disponivel):
        return Motorista(nome=nome, veiculo=veiculo, disponivel=True)

    def criar_passageiro(self, nome, local_paetida, destino):
        raise NotImplementedError("DrivenFactory não cria passageiros.")

    def criar_corrida(self, driver, passenger, distance):
        raise NotImplementedError("DrivenFactoryes não cria corridas.")
