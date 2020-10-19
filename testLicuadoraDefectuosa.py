import unittest
from licuadoraDefectuosa import LicuadoraDefectuosa

class TestLicuadoraDefectuosa(unittest.TestCase):
    def test_rebalsar(self):
        lic = LicuadoraDefectuosa( 1500, "blanca", 800, 2000, 500, 1800)
        print (lic.capacidad)
        self.assertEqual(lic.agregarLiquido(600), "La licuadora está llena y se derramaron 100 mililitros")
    def test_agregar200(self):
        licu = LicuadoraDefectuosa( 1500, "blanca", 800, 2000, 500, 1800)
        licu.agregarLiquido(200)
        self.assertTrue(licu.contenido == 200)
    def test_usar10(self):
        licu = LicuadoraDefectuosa( 1500, "blanca", 800, 2000, 500, 1800)
        licu.usar(10)
        self.assertTrue(licu.horas_de_uso == 20)
    def test_usar50(self):
        licu = LicuadoraDefectuosa( 1500, "blanca", 800, 2000, 500, 1800)
        licu.usar(50)
        self.assertTrue(licu.horas_de_uso == 100)


if __name__ == '__main__':
    unittest.main()
