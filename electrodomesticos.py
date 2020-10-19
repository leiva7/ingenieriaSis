tipos = ["lavarropas", "microondas", "heladera", "minicomponente", "licuadora"]

class Electrodomestico:
    """Genera un electrodomestico"""

    def __init__(self, precio, tipo, color, peso, consumo_energetico):
        # Precio expresado en pesos, peso expresado en kg, consumo en wh
        self.precio = precio
        self.tipo = self.tipo_de_electrodomestico(tipo)
        self.color = color
        self.peso = peso
        self.consumo_energetico = consumo_energetico
        self.horas_de_uso = 0
        
    def get_uso(self):
        return self.horas_de_uso

    def tipo_de_electrodomestico(self, tipo):
        """Permite establecer el tipo de electrodomestico. Los tipos pueden
        ser aquellos definidos en el array de la variable tipos 
        """
        while tipo not in tipos:
            print("El tipo seleccionado: *", tipo, "* no es valido.")
            print("Por favor establezca un tipo válido, a saber: ")
            for i in tipos:
                print(i)
            tipo = input()
        if tipo in tipos:
            return tipo

    def caracteristicas(self):
        """Imprime las características del electrodomestico"""
        print("Color: ", self.color, " Tipo: ", self.tipo, " Peso: ",  self.peso, "kgs", " Precio: $", self.precio)

    def usar(self, horas):
        """Aumenta la cantidad de horas de uso del electrodomestico segun lo indicado"""
        self.horas_de_uso += horas

    def costo_hasta_ahora(self, preEnergia):
        """Calcula el costo de uso acumulado hasta ahora, tomando el 
        costo actual de la energia
        """
        #  precio energia a razon de kwh, mientras que consumo en wh
        return(self.horas_de_uso * self.consumo_energetico)/1000 * preEnergia

class Lavarropas(Electrodomestico):
    """Clase lavarropas"""
    def __init__(self, precio, color, peso, consumo_energetico, capacidad, cantProgramas):
        Electrodomestico.__init__(self, precio, "lavarropas", color, peso, consumo_energetico)
        self.capacidad = capacidad
        self.cantProgramas = cantProgramas
        self.jabon = 0
        
    def funcionar(self, programa):
        """El lavarropa funciona de acuerdo al programa especificado"""
        if programa >= 1 and programa <= self.cantProgramas:
            print("Funcionando en el programa de lavado ", programa)
        else:
            print("Elija un programa de lavado válido")
    
    def cargarJabon(self, cantJabon):
        """Toma una cant de jabon en grs y lo carga al lavarropas"""
        self.jabon += cantJabon
    
    def get_jabon(self):
        return self.jabon
    
class Microondas(Electrodomestico):
    """Clase Microondas"""
    def __init__(self, precio, color, peso, consumo_energetico, menues):
        Electrodomestico.__init__(self, precio, "microondas", color, peso, consumo_energetico)
        self.menues = menues
        
    def funcionar(self, menu, segundos):
        """El microondas funciona de acuerdo al menu y tiempo en segundos indicado"""
        if menu > 0 and menu <= self.menues:
            print("El microondas funciona en programa ", menu, " durante ", segundos, " segundos")
        else:
            print("Por favor seleccione un menú valido, entre 0 y ", self.menues)
            
    def abrirPuerta (self):
        """El microondas abre sus puertas"""
        print("La puerta del microondas se abrio")
        
class LicuadoraDefectuosa(Electrodomestico):
    """Clase licuadora defectuosa"""
    def __init__(self, precio, color, peso, consumo_energetico, capacidad, potencias):
        Electrodomestico.__init__(self, precio, "licuadora", color, peso, consumo_energetico)
        self.capacidad = capacidad #en mililitros
        self.potencias = potencias
        self.contenido = 0
        
    def agregarLiquido(self, mililitros):
        """Se agregan liquidos a la licuadora en mililitros. Rebalsa
        si supera la capacidad
        """
        if self.contenido + mililitros > self.capacidad:
            print("La licuadora está llena y se derramaron ", (self.contenido + mililitros - self.capacidad) ," mililitros")
            return ("La licuadora está llena y se derramaron "+ str(self.contenido + mililitros - self.capacidad) +" mililitros")
            self.contenido = self.capacidad
        else:
            self.contenido += mililitros
            
    def usar(self, horas):
        """Aumenta la cantidad de horas de uso de la licuadora
        el doble de lo indicado por su defecto
        """
        self.horas_de_uso += horas*2
        