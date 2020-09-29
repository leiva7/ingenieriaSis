import unittest
import herenciaMultiple2
import electrodomesticos

class TestDocentePractico(unittest.TestCase):
    def test_examenMatematicaOk(self):
        marce = herenciaMultiple2.DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        marce.set_materia("Matemática")
        self.assertEqual(marce.dar_clase("Unidad 7"), "Cuánta plata gastaste si hiciste 10km en un auto que consume 1.5 litros por cada kilómetro y la nafta cuesta 50 pesos por litro? 1) 800, 2) 750, 3) 500")

    def test_examenArteNone(self):
        marce = herenciaMultiple2.DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        marce.set_materia("Arte")
        self.assertEqual(marce.dar_clase("Unidad 7"), None)

    def test_corregir100(self):
        marce = herenciaMultiple2.DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        self.assertEqual(marce.corregir([(2,2),("Arabia","Arabia"),(7,7),("Ley de Ohm","Ley de Ohm")]), "Porcentaje de rtas correctas: 100.0")
    
    def test_corregir50(self):
        marce = herenciaMultiple2.DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        self.assertEqual(marce.corregir([(2,1),("Arabia","Arabia"),(7,7),("Ley de Ohm","Matemáticas")]), "Porcentaje de rtas correctas: 50.0")
        
class TestLicuadoraDefectuosa(unittest.TestCase):
    def test_rebalsar(self):
        lic = electrodomesticos.LicuadoraDefectuosa( 1500, "blanca", 800, 2000, 500, 1800)
        print (lic.capacidad)
        self.assertEqual(lic.agregarLiquido(600), "La licuadora está llena y se derramaron 100 mililitros")
    def test_agregar200(self):
        licu = electrodomesticos.LicuadoraDefectuosa( 1500, "blanca", 800, 2000, 500, 1800)
        licu.agregarLiquido(200)
        self.assertTrue(licu.contenido == 200)
    def test_usar10(self):
        licu = electrodomesticos.LicuadoraDefectuosa( 1500, "blanca", 800, 2000, 500, 1800)
        licu.usar(10)
        self.assertTrue(licu.horas_de_uso == 20)
    def test_usar50(self):
        licu = electrodomesticos.LicuadoraDefectuosa( 1500, "blanca", 800, 2000, 500, 1800)
        licu.usar(50)
        self.assertTrue(licu.horas_de_uso == 100)


if __name__ == '__main__':
    unittest.main()
