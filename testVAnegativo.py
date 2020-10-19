import unittest
from va import valorabsoluto

class TestSut(unittest.TestCase):

    def test_valorAbsoluto1(self):
        self.assertEqual(valorabsoluto(-7),7)
        

if __name__ == '__main__':
    unittest.main()
