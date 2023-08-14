monto = int(input("Ingrese el monto total de la compra: "))

if monto > 3500:
    total = monto - (monto *0.10)
    print(f"Su monto final es de: ${total}")
else:
    print(f"Su monto final es el mismo, no recibe ningun descuento: ${monto}")
