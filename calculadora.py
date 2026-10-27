
def sumar(a, b):
    return a + b


def resta(a, b):
    return a - b


def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b


def calcular_area_circulo(radio):
    return 3.1416 * radio ** 2


def calcular_area_cuadrado(lado):
    return lado * lado


def calcular_area_triangulo(base, altura):
    return base * altura / 2
