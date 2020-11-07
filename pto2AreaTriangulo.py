import sut
import unittest
from unittest.mock import MagicMock

class TestBase(unittest.TestCase):
    
    def testAreaTrianguloEntero(self):
        sut.multiplicar = MagicMock(return_value=50)
        sut.dividir = MagicMock(return_value=25)
        a = sut.area_triangulo(10, 5)
        
        esperado = 25
        self.assertEqual(a, esperado)
		
    def testAreaTrianguloDecimal(self):
        sut.multiplicar = MagicMock(return_value=15)
        sut.dividir = MagicMock(return_value=7.5)
        a = sut.area_triangulo(3, 5)
        
        esperado = 7.5
        self.assertEqual(a, esperado)
        
        
if __name__ == '__main__':
    unittest.main()