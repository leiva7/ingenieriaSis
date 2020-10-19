# Punto 1
Si se realiza el testeo con los archivos [testVAnegativo](testVAnegativo.py) y [testVApositivo](testVApositivo.py) y se lo analiza con coverage, se puede ver que en ambos casos nada queda excluido ni sin recorrer, alcanzando 100% de cobertura (NOTA: Me parece que no subió el archivo con las modificaciones de sut.py)
Captura negativo: ![imagen coverage testVAnegativo](https://drive.google.com/file/d/175Fh5enfQrw4OMsONfm6eV1EfySE_rCE/view?usp=sharing)
Captura positivo: ![imagen coverage testVApositivo](https://drive.google.com/file/d/1PgayGhgBbfKuHHEDnnXsrTIFwiMU1Hbx/view?usp=sharing)

# Punto 2
No había ningún test definido para comparar, por lo que se procede directamente a generar uno que cubra el 100%
(Nota: acá tuve un problema, está todo en el test pero no me está ingresando a un par de líneas, dejo imagenes más detalladas)
Captura coverage test: ![imagen de cobertura del test de comparar](https://drive.google.com/file/d/1-mcWTFuC6AUBhdBlAbjoIpuZ4ZjGTmmQ/view?usp=sharing)
Captura coverage comparar: ![imagen cobertura de comparar](https://drive.google.com/file/d/1VH-35RjxiOLlFOGMFKCNCzUXwE9wXXGQ/view?usp=sharing)

# Punto 3
Se establecen test para la LicuadoraDefectuosa y el DocentePractico que cubran más del 83%
Los archivos de los test son [testDocentePractico](testDocentePractico.py) y [testLicuadoraDefectuosa](testLicuadoraDefectuosa.py).
Las capturas de coverage:
![imagen coverage docentePractico](https://drive.google.com/file/d/1G46Ci-TaRnN9U-yolbIsvpoceAc3eDtZ/view?usp=sharing)
![imagen coverage licuadoraDefectuosa](https://drive.google.com/file/d/1ipd5dHBOihaerULM-BAqqU8UIYMIemrx/view?usp=sharing)
