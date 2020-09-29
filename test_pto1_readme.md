# Testeo

Si se realiza el testeo del archivo [sut](sut.py) con el archivo [test_pto1](test_pto1.py) se puede ver que devuelve lo siguiente:

> ======================================================================
> ERROR: test_productoria1 (__main__.TestSut)
> ----------------------------------------------------------------------
> Traceback (most recent call last):
>  File "test_pto1.py", line 15, in test_productoria1
>    self.assertEqual(sut.productoria([4,5,6,7],3), 120)
>  File "D:\Fran\Cursos\Software ITS\Ingeniería de software\testing\sut.py", line 6,> in productoria
>    return prod(lista[:hasta])
> NameError: name 'prod' is not defined
> ----------------------------------------------------------------------
> Ran 5 tests in 0.039s
> FAILED (errors=1)

Que es un error que sucede dado que el archivo sut que importamos para testear no compila. Se identifica que ese error es porque la función "prod" se llama en la línea 15 sin haber sido definida. Por otro lado, si se comentan o borran tanto la función productoria del archivo sut como el test de la misma en el archivo de testeo, puede verse que el resto de los testeos devuelve: 

> Ran 4 tests in 0.001s
>
> OK

Que quiere decir que se ejecutaron los test correctamente y pasaron el assert.