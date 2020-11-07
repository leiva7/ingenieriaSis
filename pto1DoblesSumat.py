import sut
import unittest
from unittest.mock import MagicMock

class TestBase(unittest.TestCase):
    
    def testSumatoriaManual(self):
        valores_por_iteracion = lambda x, y: x + y
        sut.sumar = MagicMock()
        sut.sumar.side_effect = valores_por_iteracion
        a = sut.sumatoria_manual([3,2,4,7],2)
        
        esperado = 9
        self.assertEqual(a, esperado)
        
if __name__ == '__main__':
    unittest.main()
