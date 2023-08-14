from random import *


def comparar(valor, lista):
    cont = 0

    for num in lista:
        if num > valor:
            cont += 1

    return cont


def promedio_lista(lista):

    cont = 0
    sum = 0

    for num in lista:
        sum = sum + num
        cont += 1

    promedio = sum / cont
    return promedio


def max_min(lista):

    minimo = min(lista)
    maximo = max(lista)

    return maximo, minimo

# Declaracion de lista vacia
lista = []

# Agregacion de elementos a la lista
for num in range(1, 11):
    num_aleatorio = randint(1, 20)
    lista.append(num_aleatorio)

# Mostramos lista
print(f"- LISTA -\n{lista}")
valor = int(input("Ingrese un valor para compararlo con los de la lista: "))

# Mostramos numeros de la lista mayores al valor ingresado
resultado_mayores = comparar(valor, lista)
print(f"La cantidad de resultados mayores al valor ingresados son: {resultado_mayores} numeros")

# Mostramos el promedio total de la lista
resultado_promedio = promedio_lista(lista)
print(f"El promedio de la lista es de: {resultado_promedio}")

# Mostramos maximo y minimo de la lista
maximo, minimo = max_min(lista)
print(f"El valor maximo de la lista es {maximo} y el menor es {minimo}")
