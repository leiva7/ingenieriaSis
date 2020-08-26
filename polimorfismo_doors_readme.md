# Implementación y análisis de polimorfismo_doors.py

## Polimorfismo

De acuerdo a lo indicado en el módulo teórico, en python no hay sobrecarga de métodos, con lo cual no se pueden ver ejemplos de polimorfismo de la misma manera que en otros lenguajes, porque el último método declarado (con el mismo nombre que uno previo) reemplaza a los anteriores.

## Ejemplo de uso y explicación

Si tomamos el [archivo](polimorfismo_doors.py) y ejecutamos en consola las siguientes instrucciones: 

```
door = Door()  # Creación de puerta
bool_door = BooleanDoor()  # Creación de puerta bool
room = Room(door) # Creación de habitación con puerta
bool_room = Room(bool_door) # Creación de habitación  con puerta bool
room.open() # Apertura de la puerta de la habitación
#a través de un método de la habitación, que llama a
#un método de la puerta
room.is_open() # Verifica con un método de la habitación
#que llama al método de la puerta para saber si
#esta abierta
True  #devuelve verdadero a partir de la comparación con el valor de status que es un string
room.close() # Cierra la puerta de la misma forma
room.is_open() # Consulta de la misma forma
False #devuelve falso
```
```
bool_room.open() #Utiliza el método open de la habitación
#que llama al método open de la puerta bool
bool_room.is_open() #Utiliza el método is_open de la
# habitación que llama a is_open de la puerta bool
True #devuelve verdadero porque retorna el status booleano
bool_room.close() #cierra la puerta de la misa forma
bool_room.is_open() #consulta de la misma forma
False #devuelve falso
```