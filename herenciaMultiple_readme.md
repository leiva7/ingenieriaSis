# Herencia Múltiple y super()
La herencia múltiple implica que cada clase hija puede heredar de más de una clase madre.
En ese contexto, super() permite acceder a los métodos de la clase superior que este infgresada primero en la herencia.

## Ejemplo de uso y explicación 
Si tomamos el [archivo](herenciaMultiple.py) y ejecutamos las siguientes instrucciones:
```
ba = B()
```
obtenemos por resultado:
>B
>A
dado que se ejecuta print(B) que es la primera línea del __init__ de B, y lugo se llama a super() del init de A (porque es la única clase madre de B), en la cual se printeaba A.

Si ejecutamos
```
gabyRotondi = DocenteTitular("Gabriela", "Rotondi", 5333333, 60, 3333, 53, 10)
gabyRotondi.armarPrograma()
gabyRotondi.peleandoAprobacion()
gabyRotondi.set_materia("Matemática")
gabyRotondi.darClasesTP("Arboles binarios")
```
nos devuelve:
>Redactando programa
>Remando la aprobación
>Estoy dando la clase de  Arboles binarios  a mis  53  alumnos. Además propongo práctico: Cuánta plata gastaste si hiciste 10km en un auto que consume 1.5 litros por cada kilómetro y la nafta cuesta 50 pesos por litro? 1) 800, 2) 750, 3) 500

Esto ocurre porque primero se llama a los métodos propios de la clase DocenteTitular (armarPrograma() y peleandoAprobacion()), luego se llama a set_materia() que es un método heredado de DocentePractico, que a la vez lo había sobreescrito de Docente; y luego se llama a darClasesTP(), que es un método propio de DocenteTitular que a su vez llama con sueper() al método darPractico() del DocentePractico.

Ejecución disponible en: [herenciaMultiple_ejecucion.py](herenciaMultiple_ejecucion.py)
