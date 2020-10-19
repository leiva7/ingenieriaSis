from herenciaMultiple2 import Docente

class DocentePractico(Docente):
    def __init__(self, nombre, apellido, dni, edad, nLegajo, cAlumnos, antiguedad):
        Docente.__init__(self, nombre, apellido, dni, edad, nLegajo, cAlumnos, antiguedad)
    
    def set_materia(self,materia):
        if materia == "Matemática" or "Programación":
            self.materia = materia
        else:
            print("Indique una materia habilitada (Matemática, Geografía o Programación)")
            
    def dar_clase(self, unidad):
        super().dar_clase(unidad)
        #self.darClases(unidad)
        print("Además propongo práctico: ")
        if self.materia == "Matemática":
             print("Cuánta plata gastaste si hiciste 10km en un auto que consume 1.5 litros por cada kilómetro y la nafta cuesta 50 pesos por litro? 1) 800, 2) 750, 3) 500")
             return "Cuánta plata gastaste si hiciste 10km en un auto que consume 1.5 litros por cada kilómetro y la nafta cuesta 50 pesos por litro? 1) 800, 2) 750, 3) 500"
        elif self.materia == "Programación":
            print("En Python, qué valor resulta de hacer ‘a == b == a is b’ si tanto a como b tienen en valor [1, 2, 3]? 1) True, 2) False, 3) Da error")
            return "En Python, qué valor resulta de hacer ‘a == b == a is b’ si tanto a como b tienen en valor [1, 2, 3]? 1) True, 2) False, 3) Da error"