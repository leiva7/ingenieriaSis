import sut
import unittest
from unittest.mock import MagicMock
"""
class TestBase(unittest.TestCase):
    
    def testProductoriaManual(self):
        sut.multiplicar = MagicMock(return_value=24)
        a = sut.productoria_manual([3,2,4,1],3)
        
        esperado = 24
        self.assertEqual(a, esperado)
        
if __name__ == '__main__':
    unittest.main()
"""
class TestBase(unittest.TestCase):
    
    def testProductoriaManual(self):
        valores_por_iteracion = lambda x, y: x * y
        sut.multiplicar = MagicMock()
        sut.multiplicar.side_effect = valores_por_iteracion
        a = sut.productoria_manual([3,2,4,1],3)
        
        esperado = 24
        self.assertEqual(a, esperado)
        
if __name__ == '__main__':
    unittest.main()
