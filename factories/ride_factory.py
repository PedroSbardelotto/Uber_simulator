from factories.abstract_factory import abstractFactory
from models.driver import Motorista
from models.passenger import Passageiro
from models.ride import Corrida


from abc import ABC, abstractmethod

# Classe base abstrata com o Template Method
class RideTemplate(ABC):
    def criar_corrida(self, id_corrida, motorista, passageiro, distancia):
        """
        Método Template para criar uma corrida. Define os passos gerais.
        """
        if motorista is None or passageiro is None or distancia is None:
            raise ValueError("Motorista, passageiro ou distância não podem ser None")
        
        self.validar_dados(motorista, passageiro, distancia)
        preco = self.calcular_preco(distancia)
        return self.instanciar_corrida(id_corrida, motorista, passageiro, distancia, preco)

    @abstractmethod
    def validar_dados(self, motorista, passageiro, distancia):
        """
        Método abstrato para validação específica de dados.
        """
        pass

    @abstractmethod
    def calcular_preco(self, distancia):
        """
        Método abstrato para cálculo do preço da corrida.
        """
        pass

    @abstractmethod
    def instanciar_corrida(self, id_corrida, motorista, passageiro, distancia, preco):
        """
        Método abstrato para criar a instância de corrida específica.
        """
        pass


# Implementação para Corridas Econômicas
class RideEconomica(RideTemplate):
    def validar_dados(self, motorista, passageiro, distancia):
        if motorista['veiculo']['tipo'] != 'econômico':
            raise ValueError("Apenas motoristas com veículos econômicos podem realizar essa corrida.")

    def calcular_preco(self, distancia):
        return distancia * 1.5  # Preço fixo por km para corridas econômicas

    def instanciar_corrida(self, id_corrida, motorista, passageiro, distancia, preco):
        return {
            "id_corrida": id_corrida,
            "tipo": "Econômica",
            "motorista": motorista,
            "passageiro": passageiro,
            "distancia": distancia,
            "preco": preco,
        }


# Implementação para Corridas de Luxo
class RideLuxo(RideTemplate):
    def validar_dados(self, motorista, passageiro, distancia):
        if motorista['veiculo']['tipo'] != 'luxo':
            raise ValueError("Apenas motoristas com veículos de luxo podem realizar essa corrida.")

    def calcular_preco(self, distancia):
        return distancia * 3.0  # Preço fixo por km para corridas de luxo

    def instanciar_corrida(self, id_corrida, motorista, passageiro, distancia, preco):
        return {
            "id_corrida": id_corrida,
            "tipo": "Luxo",
            "motorista": motorista,
            "passageiro": passageiro,
            "distancia": distancia,
            "preco": preco,
        }


# Testando as implementações
if __name__ == "__main__":
    motorista_economico = {"nome": "João", "veiculo": {"tipo": "econômico"}}
    motorista_luxo = {"nome": "Ana", "veiculo": {"tipo": "luxo"}}
    passageiro = {"nome": "Carlos", "local_partida": "A", "destino": "B"}

    corrida_economica = RideEconomica()
    corrida_luxo = RideLuxo()

    try:
        corrida1 = corrida_economica.criar_corrida(
            id_corrida=1,
            motorista=motorista_economico,
            passageiro=passageiro,
            distancia=10
        )
        print("Corrida Econômica Criada:", corrida1)

        corrida2 = corrida_luxo.criar_corrida(
            id_corrida=2,
            motorista=motorista_luxo,
            passageiro=passageiro,
            distancia=10
        )
        print("Corrida de Luxo Criada:", corrida2)
    except ValueError as e:
        print("Erro ao criar corrida:", e)
