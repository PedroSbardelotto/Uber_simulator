class Corrida:
    def __init__(self, id_corrida, motorista, passageiro, distancia):
        self.id_corrida = id_corrida
        self.motorista = motorista
        self.passageiro = passageiro
        self.distancia = distancia  # em quilômetros
        self.status = "solicitada"
        self.valor = 0.0

    def iniciar_corrida(self):
        if not self.motorista.disponivel:
            raise Exception("Motorista indisponível")
        self.status = "em andamento"
        self.motorista.atualizar_status(False)

    def finalizar_corrida(self):
        if self.status != "em andamento":
            raise Exception("A corrida ainda não foi iniciada")
        self.status = "finalizada"
        self.valor = self.calcular_valor()
        self.motorista.atualizar_status(True)

    def calcular_valor(self):
        taxa_base = 5.0  # Taxa fixa inicial
        valor_por_km = 2.5  # valor por quilômetro
        return taxa_base + (valor_por_km * self.distancia)

    def __repr__(self):
        return (f"Corrida(id = {self.id_corrida}, motorista = {self.motorista.nome}, "
                f"passageiro = {self.passageiro.nome}, status = {self.status}, valor = {self.valor})")
