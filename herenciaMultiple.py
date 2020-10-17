class A(object):
    def __init__(self):
        print("A")
        super(A, self).__init__()
        
class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()
        

class Persona():
    def __init__(self, nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
     
    def habla(self, decir):
        print(decir)

class Docente(Persona):
    def __init__(self, nombre, apellido, dni, edad, nLegajo, cAlumnos, antiguedad):
        Persona.__init__(self, nombre, apellido, dni, edad)
        self.materia = ""
        self.nLegajo = nLegajo
        self.cAlumnos = cAlumnos
        self.antiguedad = antiguedad
        
    def set_materia(self,materia):
        if materia == "Geografía" or "Matemática" or "Programación":
            self.materia = materia
        else:
            print("Indique una materia habilitada (Matemática, Geografía o Programación)")
            
    def corregir(self, listaTuplas):
        cantPreguntas = 0
        correctas = 0
        for t in listaTuplas:
            cantPreguntas += 1
            if t[0] == t[1]:
                correctas += 1
        porcentajeCorrectas = (correctas * 100)/cantPreguntas
        print("Porcentaje de rtas correctas: ", porcentajeCorrectas )
        
    def darClases(self, unidad):
        print("Estoy dando la clase de ", unidad, " a mis ", self.cAlumnos, " alumnos.")
            
class DocenteTeorico(Docente):
    def __init__(self, nombre, apellido, dni, edad, nLegajo, cAlumnos, antiguedad):
        Docente.__init__(self, nombre, apellido, dni, edad, nLegajo, cAlumnos, antiguedad)
        
    def dar_clase(self, unidad):
        print("Estoy dando la clase de ", unidad, " a mis ", self.cAlumnos, " alumnos")
        
    def proponerExamen(self):
        if self.materia == "Geografía":
            print("Cuál es el rio más ancho del mundo? 1) De la plata, 2) Nylo, 3) Amazonas")
        elif self.materia == "Matemática":
             print("Cuántos lados tiene un polígono? 1) 5, 2) más de 2, 3) 5 o más")
        elif self.materia == "Programación":
            print("Qué es Scrum? 1) Una forma de escribir código, 2) una metodología ágil, 3) una herramienta de debugging")

       
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
        print("Además propongo práctico: ")
        if self.materia == "Matemática":
             print("Cuánta plata gastaste si hiciste 10km en un auto que consume 1.5 litros por cada kilómetro y la nafta cuesta 50 pesos por litro? 1) 800, 2) 750, 3) 500")
        elif self.materia == "Programación":
            print("En Python, qué valor resulta de hacer ‘a == b == a is b’ si tanto a como b tienen en valor [1, 2, 3]? 1) True, 2) False, 3) Da error")
            
class DocenteTitular(DocentePractico, DocenteTeorico):
    def __init__(self, *args):
        super(DocenteTitular, self).__init__(*args)
    
    def armarPrograma(self):
        print("Redactando programa")
        
    def peleandoAprobacion(self):
        print("Remando la aprobación de la materia")
        
    def dar_clase(self, unidad):
        super(DocenteTitular, self).dar_clase(unidad)
        

        
