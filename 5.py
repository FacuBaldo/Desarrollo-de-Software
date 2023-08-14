nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 13 and edad < 15:
    print(f"{nombre} su categoria es infantil")

elif edad >= 15 and edad < 17:
    print(f"{nombre} su categoria es cadete")

elif edad >= 17 and edad < 19:
    print(f"{nombre} su categoria es juvenil")

elif edad >= 19 and edad < 100:
    print(f"{nombre} su categoria es mayores")

else:
    print("Edad no valida")
