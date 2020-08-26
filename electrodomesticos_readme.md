# Implementación y análisis de electrodomésticos

## Polimorfismo

De acuerdo a lo indicado en el módulo teórico, en python no hay sobrecarga de métodos, con lo cual no se pueden ver ejemplos de polimorfismo de la misma manera que en otros lenguajes, porque el último método declarado (con el mismo nombre que uno previo) reemplaza a los anteriores.

## Ejemplo con clases de electrodomésticos
Se realiza a continuación la ejecución del [archivo](electrodomesticos_ejecucionej.py), en el cual se instancian los electrodomésticos disponibles y ejecutan sus métodos, importando las clases del archivo [electrodomesticos.py](electrodomesticos.py)

Al ejecutarse:
```
from electrodomesticos import *

laverrap = Lavarropas(4500, "blanco", 35, 60, 5, 12)
laverrap.funcionar(15)
laverrap.funcionar(10)
laverrap.cargarJabon(100)
print ("laverrap tiene cargado ", laverrap.get_jabon(), " grs de jabon")
```
 el programa devuelve:
>Elija un programa de lavado válido
>Funcionando en el programa de lavado 10
>laverrap tiene cargado 100 grs de jabon

Al ejecutarse:
```
atmaMicro = Microondas(15000, "blanco", 5, 640, 8)
atmaMicro.funcionar(9,120)
atmaMicro.funcionar(5, 120)
atmaMicro.abrirPuerta()
```
el programa devuelve:
>Por favor seleccione un menú valido, entre 0 y 8
>El microondas funciona en programa 5 durante 120 segundos
>La puerta del microondas se abrio

Al ejecutarse:
```
phillipsLic = LicuadoraDefectuosa(7600, "negra", 2, 600, 5000, 600)
phillipsLic.agregarLiquido(2000)
phillipsLic.agregarLiquido(3500)
phillipsLic.usar(3)
print(phillipsLic.get_uso())
```
el programa devuelve:
>La licuadora está llena y se derramaron 500 mililitros
>6
"6" en esa ejecución representa que el método usar() de la clase Electrodomesticos fue sobre escrito por el metodo usar() de la clase hija LicuadoraDefectuosa
 