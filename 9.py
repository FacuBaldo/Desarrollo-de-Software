from os import system


def menu():
    num = (input('''
1. Ingresar valor 1
2. Ingresar valor 2
3. Mostrar suma
4. Mostrar resta
5. Mostrar multiplicación
6. Mostrar división
7. Salir
Elija una opción: '''))
    return num


print("- MENU -")
num1 = menu()
while num1 != 1:
    print("Error: Debes de ingresar el primer numero para poder realizar una operacion")
    num1 = menu()
system("cls")
numA = int(input("Ingrese el numero 1: "))
system("cls")


num2 = menu()
while num2 != 2:
    print("Error: Debes de ingresar el segundo numero para poder realizar una operacion")
    num2 = menu()
system("cls")
numB = int(input("Ingrese el numero 2: "))
system("cls")


num3 = menu()
match num3:
    case "3":
        suma = numA + numB
        print(f"El resultado de la suma es: {suma}")

    case "4":
        resta = numA - numB
        print(f"El resultado de la resta es: {resta}")

    case "5":
        multiplicacion = numA * numB
        print(f"El resultado de la multiplicacion es: {multiplicacion}")

    case "6":
        division = numA / numB
        print(f"El resultado de la division es: {division}")

    case "7":
        print("FINAL")




    

        
    

