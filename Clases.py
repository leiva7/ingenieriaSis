class Bolsa:
    def __init__(self, tamanio):
        self.datos = []
        self.tamanio = tamanio

    def agregar(self, x):
        if self.tamanio > len(self.datos):
            self.datos.append(x)

    def espacio_disponible(self):
        return self.tamanio-len(self.datos)

    def ver_elementos(self):
        for e in self.datos:
            print(e)


bolsita = Bolsa(10)
bolsita.agregar(1)
print(bolsita.espacio_disponible())
bolsita.ver_elementos()


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def cumpleanios(self):
        self.edad += 1

    def comotellamas(self):
        print("Me llamo ", self.nombre, " ", self.apellido)


franco = Persona("Franco", "Leiva", 28)
paula = Persona("Paula", "Montesino", 32)
jesica = Persona("Jesica", "Suarez", 22)
paola = Persona("Paola", "Tabare", 22)
paola.cumpleanios()
paola.comotellamas()


class Auto:
    def __init__(self, marca, modelo, consumo):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = 0
        self.consumo = consumo

    def viaje(self, km):
        self.kilometraje += km

    def cuantogaste(self, precioNafta):
        return self.kilometraje*self.consumo*precioNafta


coche = Auto("Nissan", "March", 0.067)
coche.viaje(250)
coche.cuantogaste(62)
