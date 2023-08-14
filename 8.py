import random

def generar_lista_de_atletas():
    lista_atletas = []
    nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
    apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')
    for i in range(1, 21):
        atleta = {
            "nombre": random.choice(nombres) + " " + random.choice(apellidos),
            "numero": i,
            "tiempo_llegada": random.random() * 120
        }
        lista_atletas.append(atleta)
    return lista_atletas


lista = generar_lista_de_atletas()


def mostrar_atletas(lista):
    for atleta in lista:
        print(f"Nombre: {atleta['nombre']}, Numero: {atleta['numero']}, Tiempo llegada: {atleta['tiempo_llegada']}")


mostrar_atletas(lista)


def atleta_ganador(lista):
    
    tiempo = 15000000000

    for atleta in lista:
        if(atleta['tiempo_llegada'] < tiempo):
            tiempo = atleta['tiempo_llegada']
            numero_atleta = atleta["numero"]
    
    return numero_atleta

numero_ganador = atleta_ganador(lista)
print(f"El numero del atleta ganador es: {numero_ganador}")


def mostrar_datos_atleta(numero, lista):
    
    for atleta in lista:

        if(atleta['numero'] == numero):
            print(f"Nombre: {atleta['nombre']}, Numero: {atleta['numero']}, Tiempo llegada: {atleta['tiempo_llegada']}")


numero = int(input("Ingrese el numero de atleta a buscar: "))
mostrar_datos_atleta(numero, lista)

def podio (lista):

    mi_tupla = ()
    tiempoA = 15000000000
    tiempoB = 15000000000
    tiempoC = 15000000000

    for atleta in lista:

        if(atleta['tiempo_llegada'] < tiempoA):
            tiempoA = atleta['tiempo_llegada']
            numero_atleta = atleta["numero"]
    
    for atleta in lista:
        if(atleta['tiempo_llegada'] < tiempoB and atleta['tiempo_llegada'] > tiempoA):
            tiempoB = atleta['tiempo_llegada']
            numero_atleta = atleta["numero"]
    
    for atleta in lista:
        if(atleta['tiempo_llegada'] < tiempoC and atleta['tiempo_llegada'] > tiempoA and atleta['tiempo_llegada'] > tiempoB):
            tiempoC = atleta['tiempo_llegada']
            numero_atleta = atleta["numero"]
    
    mi_tupla = (tiempoA, tiempoB, tiempoC)
    return mi_tupla


tupla = podio(lista)
print(f"El podio de tiempo es: {tupla}")

