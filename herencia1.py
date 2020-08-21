class Vehiculo():
    def __init__(self, caballosdefuerza):
        self.caballosdefuerza = caballosdefuerza
        
    def arrancar(self):
        print("Arranca el vehículo")
        
    def frenar(self):
        print("Frena el vehículo")
        

class Automovil(Vehiculo):
    def __init__(self, caballosdefuerza, cantidadpuertas):
        Vehiculo.__init__(self, caballosdefuerza)
        self.cantidadpuertas = cantidadpuertas
        
    def abrirpuerta(self):
        print("Abro una de las ", self.cantidadpuertas, " puertas")
        
    def cierropuerta(self):
        print("Cierro una de las ", self.cantidadpuertas, " puertas")
        
class PalaMecanica(Vehiculo):
    def __init__(self, caballosdefuerza, pesomaximo):
        Vehiculo.__init__(self, caballosdefuerza)
        self.pesomaximo = pesomaximo
        
    def levantarpala(self):
        print("Subo hasta ", self.pesomaximo, " kilos")
        
    def bajarpala(self):
        print("Bajo hasta ", self.pesomaximo, " kilos")

fiat = Automovil(107, 4)
fiat.arrancar()
fiat.frenar()
fiat.abrirpuerta()
fiat.cierropuerta

pala = PalaMecanica(120, 2000)
pala.arrancar()
pala.frenar()
pala.levantarpala()
pala.bajarpala()


class Instrumento():
    def __init__(self, tipo):
        self.tipo = tipo
        
    def sonar(self):
        print(self.tipo, " sonando")
        
    def afinar(self):
        print("Instrumento afinado")
        
class Guitarra(Instrumento):
    def __init__(self, tipo, cuerda):
        Instrumento.__init__(self, tipo)
        self.cuerda = cuerda
        
    def punteo(self):
        print(self.tipo, " tocando punteo")
    
class Piano(Instrumento):
    def __init__(self, tipo, teclas):
        Instrumento.__init__(self, tipo)
        self.teclas = teclas
        
    def concierto(self):
        print("Concierto de ", self.tipo)
        
class Saxo(Instrumento):
    def __init__(self, tipo, tamanio):
        Instrumento.__init__(self, tipo)
        self.tamanio = tamanio
        
    def escala(self):
        print("Escala de ", self.tipo)
        
fender = Guitarra("guitarra", 5)
fender.sonar()
fender.afinar()
fender.punteo()

yamaha = Piano("piano", 36)
yamaha.sonar()
yamaha.afinar()
yamaha.concierto()

saxoCloacal = Saxo("saxo","grande")
saxoCloacal.sonar()
saxoCloacal.afinar()
saxoCloacal.escala()
