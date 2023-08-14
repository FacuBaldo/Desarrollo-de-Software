sum = 0

for num in range(0,5):

    temp = int(input(f"Ingrese la temperatura del num {num + 1}: "))
    sum = sum + temp

promedio = sum / 5
print(f"El promedio total de la semana es de {promedio}ºC")
