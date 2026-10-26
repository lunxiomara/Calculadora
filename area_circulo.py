def calcular_area_circulo(radio):
    area = 3.1416 * radio ** 2
    return area

radio = float(input("Ingresa el radio del círculo: "))
print("El área del círculo es:", calcular_area_circulo(radio))