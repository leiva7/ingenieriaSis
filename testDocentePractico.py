import unittest
from docentePractico import DocentePractico

class TestDocentePractico(unittest.TestCase):
    def test_examenMatematicaOk(self):
        marce = DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        marce.set_materia("Matemática")
        self.assertEqual(marce.dar_clase("Unidad 7"), "Cuánta plata gastaste si hiciste 10km en un auto que consume 1.5 litros por cada kilómetro y la nafta cuesta 50 pesos por litro? 1) 800, 2) 750, 3) 500")

    def test_examenArteNone(self):
        marce = DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        marce.set_materia("Arte")
        self.assertEqual(marce.dar_clase("Unidad 7"), None)

    def test_corregir100(self):
        marce = DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        self.assertEqual(marce.corregir([(2,2),("Arabia","Arabia"),(7,7),("Ley de Ohm","Ley de Ohm")]), "Porcentaje de rtas correctas: 100.0")
    
    def test_corregir50(self):
        marce = DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        self.assertEqual(marce.corregir([(2,1),("Arabia","Arabia"),(7,7),("Ley de Ohm","Matemáticas")]), "Porcentaje de rtas correctas: 50.0")
        
    def test_deMatematica(self):
        marce = DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        marce.set_materia("Matemática")
        self.assertEqual(marce.materia, "Matemática")
        print(marce.materia)
    
    def test_darClaseProgram(self):
        marce = DocentePractico("Marcelo", "Corona", 55444222, 45, 55444222, 5, 4)
        marce.set_materia("Programación")
        self.assertEqual(marce.dar_clase("Unidad 7"), "En Python, qué valor resulta de hacer ‘a == b == a is b’ si tanto a como b tienen en valor [1, 2, 3]? 1) True, 2) False, 3) Da error")
        

if __name__ == '__main__':
    unittest.main()
