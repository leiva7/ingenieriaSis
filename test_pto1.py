import unittest
import sut

class TestSut(unittest.TestCase):
    def test_saludar1(self):
        self.assertEqual(sut.saludar("Franco"), "Hola Franco")

    def test_sumar1(self):
        self.assertEqual(sut.sumar(7,1), 8)

    def test_sumatoria1(self):
        self.assertEqual(sut.sumatoria([4,5,6,7],3), 15)
    
    def test_productoria1(self):
        self.assertEqual(sut.productoria([4,5,6,7],3), 120)
        
    def test_valorAbsoluto1(self):
        self.assertEqual(sut.valorabsoluto(-7),7)
        


if __name__ == '__main__':
    unittest.main()
