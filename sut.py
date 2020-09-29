import math
from collections import defaultdict


def productoria(lista, hasta):
    return prod(lista[:hasta])

def sumatoria(lista, hasta):
    return sum(lista[:hasta])

def area(ancho, alto):
    return ancho * alto

def saludar(nombre):
    return "Hola " + nombre

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def valorabsoluto(n):
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
