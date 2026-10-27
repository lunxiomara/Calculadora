def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

lado = float(input("Ingresa el lado del cuadrado: "))
print("El área del cuadrado es:", calcular_area_cuadrado(lado))