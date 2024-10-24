class Motorista:
    def __init__(self, nome, veiculo, disponivel=True):
        self.nome = nome
        self.veiculo = veiculo
        self.disponivel = disponivel

    def atualizar_status(self, disponivel):
        self.disponivel = disponivel