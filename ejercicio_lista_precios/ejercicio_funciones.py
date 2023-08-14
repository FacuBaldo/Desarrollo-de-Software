from db_productos import cargar_productos
productos = []
productos = cargar_productos()

def mostrar_productos(productos):
    for prod in productos:
        print(f"{prod['id']}")
        print(f"{prod['nombre']} ${prod['precio']}")

def calcular_precio_actualizado(precio_anterior, aumento):
    nuevo_precio = precio_anterior * aumento
    return nuevo_precio

def actualizar_precios(lista_productos, aumento):
    for producto in lista_productos:
        nuevo_precio = calcular_precio_actualizado(producto['precio'], aumento) 
        producto['precio'] = nuevo_precio


if __name__ == '__main__':
    # TODO #5a: mostrar la lista cargada
    mostrar_productos(productos)
    # TODO #5b: el usuario debe ingresar el porcentaje de aumento
    aumento = int(input("Ingrese el aumento: "))
    # TODO #5c: usar la función actualizar_precios() para actualizar los precios de la lista
    actualizar_precios(productos, aumento)
    # TODO #5d: mostrar la lista con los precios actualizados
    mostrar_productos(productos)