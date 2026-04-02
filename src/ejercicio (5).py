peso = float(input("Ingrese el peso del paquete (KG): "))
lista_zonas = ["local", "regional", "nacional"]
zona = input(f"Ingrese la zona de destino ({'/'.join(lista_zonas)}):")
if lista_zonas.__contains__(zona.lower()):
    if zona == lista_zonas[0]:
        if peso < 1:
            costo = 500
        elif peso <= 5:
            costo = 1000
        else:
            costo = 2000
    elif zona == lista_zonas[1]:
        if peso < 1:
            costo = 1000
        elif peso <= 5:
            costo = 2500
        else:
            costo = 5000
    else:
        if peso < 1:
            costo = 2000
        elif peso <= 5:
            costo = 5000
        else:
            costo = 8000
    print (f"Costo del envío es: ${costo}")
else:
    print (f"Zona no valida. Las zonas validas son: {', '.join(lista_zonas)} ")