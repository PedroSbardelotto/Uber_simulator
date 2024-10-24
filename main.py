from factories.driver_factory import DriverFactory
from factories.passenger_factory import PassengerFactoryes
from factories.ride_factory import Ridefactory

# Criar as fábricas
driver_factory = DriverFactory()
passenger_factory = PassengerFactoryes()
ride_factory = Ridefactory()

# Criar motorista
motorista = driver_factory.criar_motorista("Carlos", "Carro X", True)

# Criar passageiro
passageiro = passenger_factory.criar_passageiro("Ana", "Centro",)

# Definir distância da corrida
distancia = 15

# Criar corrida (definindo o ID da corrida)
corrida = ride_factory.criar_corrida(id_corrida= 1, motorista= motorista, passageiro= passageiro, distancia= distancia)

# Verificar se a corrida foi criada corretamente
if corrida is not None:
    try:
        # Iniciar corrida
        corrida.iniciar_corrida()
        print(f"Iniciando: {corrida}")

        # Finalizar corrida
        corrida.finalizar_corrida()
        print(f"Finalizada: {corrida}")

        # Mostrar o valor calculado
        print(f"Preço da corrida: R${corrida.valor:.2f}")

    except Exception as e:
        print(f"Erro na corrida: {e}")
else:
    print("Erro ao criar a corrida")