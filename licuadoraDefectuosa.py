from electrodomesticos import Electrodomestico
        
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
        