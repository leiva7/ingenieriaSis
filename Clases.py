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
yesica = Persona("Yesica", "Suarez", 22)
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


class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self.cantidad = 0

    def ingresar(self, cant):
        if cant >= 0:
            self.cantidad += cant

    def retirar(self, cant):
        if self.cantidad-cant < 0:
            self.cantidad = 0
        else:
            self.cantidad -= cant


# miCuenta = Cuenta("Franco")
# miCuenta.ingresar(45000)
# miCuenta.retirar(200)
# print(miCuenta.cantidad)
# miCuenta.retirar(70000)
# print(miCuenta.cantidad)


tipos = ["lavarropas", "microondas", "heladera", "minicomponente"]


class Electrodomestico:

    def __init__(self, precio, tipo, color, peso, consumo_energetico):
        # Precio expresado en pesos, peso expresado en kg, consumo en wh
        self.precio = precio
        self.tipo = self.tipo_de_electrodomestico(tipo)
        self.color = color
        self.peso = peso
        self.consumo_energetico = consumo_energetico
        self.horas_de_uso = 0

    def tipo_de_electrodomestico(self, tipo):
        while tipo not in tipos:
            print("El tipo seleccionado: *", tipo, "* no es valido.")
            print("Por favor establezca un tipo válido, a saber: ")
            for i in tipos:
                print(i)
            tipo = input()
        if tipo in tipos:
            return tipo

    def caracteristicas(self):
        print("Color: ", self.color, " Tipo: ", self.tipo, " Peso: ",  self.peso, "kgs", " Precio: $", self.precio)

    def usar(self, horas):
        self.horas_de_uso += horas

    def costo_hasta_ahora(self, preEnergia):
        #  precio energia a razon de kwh, mientras que consumo en wh
        return(self.horas_de_uso * self.consumo_energetico)/1000 * preEnergia


# miMicro = Electrodomestico(2500, "microondas", "blanco", 5, 640)
# miMicro.usar(10)
# print("costo energia hasta ahora micro ", miMicro.costo_hasta_ahora(5.35))
# miMicro.caracteristicas()
# miRadio = Electrodomestico(500, "radio", "negro", 1, 40)
# miRadio.caracteristicas()


class Libro:

    def __init__(self, isbn, titulo, autor, cantidad_de_paginas):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.cantidad_de_paginas = cantidad_de_paginas
        self.pagina_actual = 0

    def de_quien_es(self):
        print(self.autor)

    def nombre_del_titulo(self):
        print(self.titulo)

    def caracteristicas(self):
        print("Isbn: ", self.isbn, "Titulo: ", self.titulo, "Autor: ", self.autor, "Cantidad de páginas del libro: ", self.cantidad_de_paginas)

    def leer(self, pags):
        self.pagina_actual += pags
        if self.pagina_actual >= self.cantidad_de_paginas:
            print("Felicidades, terminaste!")
            self.cantidad_de_paginas = 0

    def en_que_pagina_me_quede(self):
        return self.pagina_actual


# hp = Libro(6165168, "Harry Potter", "JK. Rowling", 650)
# hp.de_quien_es()
# hp.nombre_del_titulo()
# hp.caracteristicas()
# hp.leer(50)
# print(hp.en_que_pagina_me_quede())
# hp.leer(600)


class Repartidor:

    def __init__(self, nombre, edad, salario, zona):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.zona = zona

    def plus(self, plus):
        if (self.edad < 25) and (self.zona == 3):
            print("Recibió plus!")
            self.salario += plus*self.salario/100


# rappi = Repartidor("Juan", 30, 15000, 3)
# rappi.plus(1)
# print(rappi.nombre, rappi.salario)
# go = Repartidor("Marcos", 20, 10000, 3)
# go.plus(1)
# print(go.nombre, go.salario)


class Comercial:

    def __init__(self, nombre, edad, salario, comision):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.comision = comision

    def plus(self, plus):
        if (self.edad > 30) and (self.comision > 200):
            print("Recibió plus!")
            self.salario += plus*self.salario/100


# agente = Comercial("Tatiana", 33, 25000, 300)
# agente.plus(1)
# print(agente.salario)
# agente = Comercial("Romina", 23, 25000, 100)
# agente.plus(1)
# print(agente.salario)


class Rectangulo:

    def __init__(self, vertice1, vertice2, vertice3, vertice4):
        self.v1 = vertice1
        self.v2 = vertice2
        self.v3 = vertice3
        self.v4 = vertice4

    def altura(self):
        vertices = [self.v2, self.v3, self.v4]
        for v in vertices:
            if self.v1[0] == v[0]:
                return abs(self.v1[1]-v[1])

    def base(self):
        vertices = [self.v2, self.v3, self.v4]
        for v in vertices:
            if self.v1[1] == v[1]:
                return abs(self.v1[0]-v[0])

    def superficie(self):
        return self.base()*self.altura()


# rec1 = Rectangulo((2,7),(2,1),(1,7),(1,1))
# print(rec1.altura())
# print(rec1.base())
# print(rec1.superficie())
# rec2 = Rectangulo((3,1),(3,4),(6,1),(6,4))
# print(rec2.altura())
# print(rec2.base())
# print(rec2.superficie())


class Cafetera:
    def __init__(self, cantidad_maxima):
        self.cantidad_maxima = cantidad_maxima
        self.cantidad_actual = 0

    def llenar_cafetera(self):
        self.cantidad_actual = self.cantidad_maxima

    def servir_taza(self, n):
        if self.cantidad_actual-n < 0:
            print("Me quedé sin! Solo puede servirte ", self.cantidad_actual)
            self.cantidad_actual = 0
        else:
            self.cantidad_actual -= n

    def vaciar_cafetera(self):
        self.cantidad_actual = 0

    def agregar_cafe(self, n):
        if (self.cantidad_actual+n) > self.cantidad_maxima:
            print("Te excediste de café! Solo pude agregar ", self.cantidad_maxima-self.cantidad_actual)
            self.cantidad_actual = self.cantidad_maxima
        elif n < 0:
            print("éste método agrega café! Si querés servirte, usa servir_taza")
        else:
            self.cantidad_actual += n


# arlistan = Cafetera(500)
# arlistan.llenar_cafetera()
# arlistan.servir_taza(250)
# arlistan.servir_taza(300)
# arlistan.agregar_cafe(600)
