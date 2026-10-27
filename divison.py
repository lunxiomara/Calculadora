def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("El resultado de la división es:", dividir(num1, num2))