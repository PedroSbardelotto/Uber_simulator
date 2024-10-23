import unittest
from models.ride import Corrida
from models.driver import Motorista
from models.passenger import Passageiro

class TestCorrida(unittest.TestCase):
    def setUp(self):
        """ Executado antes de cada teste: cria um motorista e um passageiro."""
        self.motorista = Motorista("Carlos", "Carro A")
        self.passageiro = Passageiro("Aline", "Centro", "Zona Sul")

    def test_iniciar_corrida(self):
        corrida = Corrida(1,self.motorista, self.passageiro, 10)
        corrida.iniciar_corrida()
        self.assertEqual(corrida.status, "em andamento")
        self.assertFalse(self.motorista.disponivel)
    
    def test_finalizar_corrida(self):
        corrida = Corrida(1,self.motorista, self.passageiro, 10)
        corrida.iniciar_corrida()
        corrida.finalizer_corrida()
        self.assertEqual(corrida.status,"finalizada")
        self.assertEqual(corrida.valor, 30.0) # 5 + (2.5 * 10)
        self.assertTrue(self.motorista.disponivel)

    def test_iniciar_corrida_com_motorista_indisponivel(self):
        self.motorista.atualizar_status(False) #Deixa o motorista ocupado
        corrida = Corrida(1, self.motorista, self.passageiro,10)
        with self.assertRaises(Exception) as context: 
            corrida.iniciar_corrida()
        self.assertEqual(str(context.exception), "Motorista indisponível")

    def test_finalizar_corrida_sem_iniciar(self):
        corrida = Corrida(1,self.motorista, self.passageiro,10)
        with self.assertRaises(Exception) as context:
            corrida.finalizer_corrida()
            self.test_finalizar_corrida()
        self.assertEqual(str(context.exception), " A corrida ainda não foi iniciada!")

if __name__ == "__main__":
    unittest.main()