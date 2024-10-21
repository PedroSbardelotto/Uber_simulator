import unittest
from models.passenger import Passageiro


class TestPassageiro(unittest.TestCase):
    def test_criar_passageiro(self):
        passageiro = Passageiro("Ana", "Centro", "Zona Sul")
        self.assertEqual(passageiro.nome, "ana")
        self.assertEqual(passageiro.local_partida, "Centro")
        self.assertEqual(passageiro.destino, "Zona Sul")

    def test_atualizar_destino(self):
        passageiro = Passageiro("Ana", "Centro", "Zona Sul")
        self.assertEqual(passageiro.nome, "ana")
        self.assertEqual(passageiro.local_partida, "Centro")
        self.assertEqual(passageiro.destino, "Zona Sul")


if __name__ == "__main__":
    unittest.main()