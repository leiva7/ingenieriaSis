# Punto 1
Si se realiza el testeo con los archivos [testVAnegativo](testVAnegativo.py) y [testVApositivo](testVApositivo.py) y se lo analiza con coverage, se puede ver que en ambos casos nada queda excluido ni sin recorrer, alcanzando 100% de cobertura (NOTA: Me parece que no subió el archivo con las modificaciones de sut.py)
Captura negativo: ![imagen coverage testVAnegativo](https://github.com/leiva7/ingenieriaSis/raw/testingCajaBlanca/vaNegativo.PNG)
Captura positivo: ![imagen coverage testVApositivo](https://github.com/leiva7/ingenieriaSis/raw/testingCajaBlanca/vaPositivo.PNG)

# Punto 2
No había ningún test definido para comparar, por lo que se procede directamente a generar uno que cubra el 100%
(Nota: acá tuve un problema, está todo en el test pero no me está ingresando a un par de líneas, dejo imagenes más detalladas)
Captura coverage test: ![imagen de cobertura del test de comparar](https://github.com/leiva7/ingenieriaSis/raw/testingCajaBlanca/comparartest.PNG)
Captura coverage comparar: ![imagen cobertura de comparar](https://github.com/leiva7/ingenieriaSis/raw/testingCajaBlanca/comparar.PNG)

# Punto 3
Se establecen test para la LicuadoraDefectuosa y el DocentePractico que cubran más del 83%
Los archivos de los test son [testDocentePractico](testDocentePractico.py) y [testLicuadoraDefectuosa](testLicuadoraDefectuosa.py).
Las capturas de coverage:
![imagen coverage docentePractico](https://github.com/leiva7/ingenieriaSis/raw/testingCajaBlanca/docente.PNG)
![imagen coverage licuadoraDefectuosa](https://github.com/leiva7/ingenieriaSis/raw/testingCajaBlanca/licuadora.PNG)
