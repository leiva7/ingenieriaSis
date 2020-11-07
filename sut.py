import math
from collections import defaultdict


def productoria(lista, hasta):
    return prod(lista[:hasta])

def sumatoria(lista, hasta):
    return sum(lista[:hasta])

def area(ancho, alto):
    return ancho * alto


def area_triangulo(base, altura):
    """
    Debe computar el area de un triangulo teniendo en cuenta la fórmula genérica
    Area = (base * altura) / 2
    """
    num = multiplicar(base, altura)

    return dividir(num, 2)


def saludar(nombre):
    return "Hola " + nombre

def sumar(a, b):
    return a + b 

def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def valorabsoluto(n):
    if n < 0:
        n = -n
    return n


def comparar(a, b):
    if a < b:
        return "A menor que B"
    if a > b:
        return "A mayor que B"
    if a == b:
        return "A y B son iguales"


def costototal(producto1, producto2):
    total = sumar(producto1, producto2)
    return "El costo total es $" + str(total)


def supercalc(num):
    exp = math.exp(num)
    sum = exp + 2
    sqrt = math.sqrt(sum)
    return sqrt



def productoria_manual(lista, hasta):
    """
    Debe computar la productoria de una lista desde el primer elemento
    hasta el elemento indicado en la pocisión <hasta>
    """
    j = 0
    result = 1
    for elem in lista:
        j += 1
        if j > hasta:
            break
        result = multiplicar(result, elem)

    return result


def sumatoria_manual(lista, hasta):
    """
    Debe computar la sumatoria de una lista desde el primer elemento
    hasta el elemento indicado en la pocisión <hasta>
    """

    j = -1
    result = 0
    for elem in lista:
        j += 1
        if j > hasta:
            break
        result = sumar(result, elem)

    return result


#print(productoria_manual([3,2,4,1],3))
#print(sumatoria_manual([3,2,4,7],2))
print (area_triangulo(10, 5))
print (area_triangulo(3, 5))