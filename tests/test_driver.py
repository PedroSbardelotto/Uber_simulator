import unittest
from models.driver import Motorista

class TestMotorista(unittest.TestCase):
    def test_criar_motorista(self):
        motorista = Motorista("Rafael", "Carro A")
        self.assertEqual(motorista.nome, "Rafael")
        self.assertTrue(motorista.disponivel)

    def Test_atualizar_satus(self):
        motorista = Motorista("Rafael", "Carro A")
        motorista.atualizar_status(False)
        self.assertFalse(motorista.disponivel)


if __name__ == "__main__":
    unittest.main()
