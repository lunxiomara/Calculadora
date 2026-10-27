def calcular_area_triangulo():
    area = base * altura / 2
    return area

base = float(input("Ingresa la base del triangulo: "))
altura = float(input("Ingresa la altura del circulo: "))
print("El area del triangulo es:", calcular_area_triangulo())