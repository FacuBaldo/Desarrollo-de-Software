cant_invitados = int(input("Ingrese la cantidad de invitados: "))
precio = int(input("Ingrese el precio del kilo de carne: "))

cant_final = cant_invitados * 0.7
precio_final = cant_final * precio

print(f"El precio final a pagar por {cant_final}kg de carne es de ${precio_final}")