class Passageiro:
    def __init__(self, nome, local_partida, destino):
        self.nome = nome
        self.local_partida = local_partida
        self.destino = destino

    def atualizar_destinos(self, novo_destino):
        self.destino = novo_destino

    def __repr__(self):
        return f"Passageiro(nome={self.nome}, partida={self.local_partida}, destino={self.destino})"
