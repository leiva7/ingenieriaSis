import unittest
from comparar import comparar

class TestSut(unittest.TestCase):

    def test_comparar(self):
        self.assertEqual(comparar(2,3),"A menor que B")
        
    def test_comparar(self):
        self.assertEqual(comparar(4,1),"A mayor que B")
        
    def test_comparar(self):
        self.assertEqual(comparar(2,2),"A y B son iguales")
        
if __name__ == '__main__':
    unittest.main()
