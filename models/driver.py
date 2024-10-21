class Motorista: 
    def __init__(self, nome, veiculo):
        self.nome = nome
        self.veiculo = veiculo
        self.disponivel = True

    def atualizar_status(self,status):
        self.disponivel = status
        