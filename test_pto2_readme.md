# Testeo

## DocentePractico()

### DocentePractico.proponerExamen(self)
De éste método se testeará:
-Que ejecutado sobre una instancia de la clase DocentePractico que tenga por valor en el atributo materia, "Matemática", retorne "Cuánta plata gastaste si hiciste 10km en un auto que consume 1.5 litros por cada kilómetro y la nafta cuesta 50 pesos por litro? 1) 800, 2) 750, 3) 500"
-Que ejecutado sobre una instancia de la clase DocentePractico que tenga por valor en el atributo materia, "Arte", no returne nada (None)

### DocentePractico.corregir(self, listaTuplas)
Se testeará:
-Que ejecutado sobre una instancia de la clase DocentePractico, pasandole la siguiente listaTuplas [(2,2),("Arabia","Arabia"),(7,7),("Ley de Ohm","Ley de Ohm")] retorne "Porcentaje de rtas correctas: 100"
-Que ejecutado sobre una instancia de la clase DocentePractico, pasandole la siguiente listaTuplas [(2,1),("Arabia","Arabia"),(7,7),("Ley de Ohm","Matemáticas")] retorne "Porcentaje de rtas correctas: 50"

## LicuadoraDefectuosa()

### LicuadoraDefectuosa.agregarLiquidos(self, mililitros)
Se testeará:
-Que ejecutado sobre una instancia de LicuadoraDefectuosa que tenga seteado su atributo capacidad en 500, al ejecutarse .agregarLiquidos(self, 600) retorne "La licuadora está llena y se derramaron 100 mililitros"
-Que ejecutado sobre una instancia de LicuadoraDefectuosa que tenga seteado su atributo capacidad en 500 y contenido en 0, al ejecutarse .agregarLiquidos(self, 200) contenido cobre el valor de 200
### LicuadoraDefectuosa.usar(self, horas)
Se testeará:
-Que ejecutado sobre una instancia de LicuadoraDefectuosa que tenga seteado su atributo horas_de_uso en 0, pasándole como parámetro 10, quede con un total de 20 horas_de_uso
-Que ejecutado sobre una instancia de LicuadoraDefectuosa que tenga seteado su atributo horas_de_uso en 0, pasándole como parámetro 50, quede con un total de 100 horas_de_uso