# Testing - Dobles

## Punto 1
Se realiza el testeo con los archivos [pto1DoblesProduc](pto1DoblesProduc.py) y [pto1DoblesSumat](pto1DoblesSumat.py) a las correspondientes funciones de [sut](sut.py)
En el primer caso, para la función productoria_manual() se identifica que arroja error ( AssertionError: 0 != 24 ) lo cual implica que hay en un error en la lógica de la función productoria. Se realiza prueba de escritorio y se identifican dos errores: que el neutro de la multiplicación es 1, por lo que result debe inicializarse en ese valor; que para que se contabilice incluyendo el elemento indicado en la posición hasta, el if debe ser j > hasta (no mayor o igual). Una vez corregido esto el test da OK.
En el segundo caso, para la función sumatoria_manual() también devuelve error ( AssertionError: 3 != 9 ). Esto indica que hay un error en la lógica de la función sumatoria_manual(). Se revisa la misma y se identifica que: para que se contabilice incluyendo el elemento indicado en la posición hasta, el if debe ser j > hasta (no mayor o igual), y j debería inicializarse en -1. Luego de esta corrección, el test devuelve OK. Sin embargo, al correr la función en el archivo de orígen sin mockear a sumar, no devuelve lo esperado (devuelve 12 para sumatoria_manual([3,2,4,7],2)  cuando debería devolver 9), motivo por el que se identifica que hay error en sumar(). Se corrige sumar para solucionar el problema. 


## Punto 2

Se realiza el testeo con el archivo [pto2AreaTriangulo](pto2AreaTriangulo.py) a la función area_triangulo de [sut](sut.py)
Se presenta el siguiente error:
> line 36, in dividir
>    return ceil(a / b)
> NameError: name 'ceil' is not defined
Se revisa la función dividir, se incluye en sut.py el prefijo math. en la llamada a ceil.
Se repite la ejecución de los test que devuelve OK. Sin embargo nuevamente cuando no se mockean las llamadas a las funciones, la que pasa por parámetros area_triangulo(3, 5) no devuelve lo esperado. Se identifica que ceil en dividir() realiza un redondeo que no debe estar; se hace la corrección. 

## Punto 3
### En qué casos se utilizan mocks y en qué casos se utiliza patch
Por lo que pude interpretar de la [documentación oficial](https://docs.python.org/3/library/unittest.mock.html) y algunas páginas más, el principal motivo para usar patch sería que facilita el reemplazo de clases u objetos durante el testeo, pero devolviendo los mismos a su estado original luego de utilizado.
Por otro lado también se indica en el material de la cátedra y en el sitio [What the mock?](https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832) que patch sirve para interceptar los módulos importados y devolver en su lugar una instancia mockeada de esos módulos configurada en el test. 
