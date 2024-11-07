from models.driver import Driver
from factories.abstract_factory import abstractFactory


class DriverFactory(abstractFactory):
    def criar_motorista(self, name, vehicle, available):
        return Driver(name=name, vehicle=vehicle, available=True)

    def criar_passageiro(self, nome, local_paetida, destino):
        raise NotImplementedError("DrivenFactory não cria passageiros.")

    def criar_corrida(self, driver, passenger, distance):
        raise NotImplementedError("DrivenFactoryes não cria corridas.")
