from factories.abstract_factory import abstractFactory
from models.driver import Motorista
from models.passenger import Passageiro
from models.ride import Corrida


class Ridefactory(abstractFactory):

    def criar_corrida(self, id_corrida, motorista, passageiro, distancia):
        if motorista is None or passageiro is None or distancia is None:
            print("Erro: Motorista, passageiro ou distância não podem ser None")
            return None
        return Corrida(id_corrida=id_corrida, motorista=motorista, passageiro=passageiro, distancia=distancia)

    def criar_passageiro(self, nome, local_paetida, destino):
        raise NotImplementedError("RideFactory não cria passageiros.")

    def criar_motorista(self, nome, veiculo):
        raise NotImplementedError("RideFactoryes não cria motorista.")
