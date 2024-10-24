class Passageiro:
    def __init__(self, nome, destino):
        self.nome = nome
        self.destino = destino

    def atualizar_destinos(self, novo_destino):
        self.destino = novo_destino

    def __repr__(self):
        return f"Passageiro(nome = {self.nome}, partida = {self.local_partida}, destino = {self.destino})"
