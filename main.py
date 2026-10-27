
from Calculadora import (
    sumar, resta, dividir,
    calcular_area_circulo,
    calcular_area_cuadrado,
    calcular_area_triangulo
)

def main():
    while True:
        print("\n=== CALCULADORA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar (pendiente)")
        print("4. Dividir")
        print("5. Calcular area de un circulo")
        print("6. Calcular area de un cuadrado")
        print("7. Calcular area de un triangulo")
        print("0. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            print("Resultado:", sumar(a, b))

        elif opcion == "2":
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            print("Resultado:", resta(a, b))

        elif opcion == "3":
            print("La multiplicacion aun no esta implementada.")

        elif opcion == "4":
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            print("Resultado:", dividir(a, b))

        elif opcion == "5":
            radio = float(input("Ingresa el radio del circulo: "))
            resultado = calcular_area_circulo(radio)
            print(f"El area del circulo es: {resultado:.2f}")

        elif opcion == "6":
            lado = float(input("Ingresa el lado del cuadrado: "))
            resultado = calcular_area_cuadrado(lado)
            print(f"El area del cuadrado es: {resultado:.2f}")

        elif opcion == "7":
            base = float(input("Ingresa la base del triangulo: "))
            altura = float(input("Ingresa la altura del triangulo: "))
            resultado = calcular_area_triangulo(base, altura)
            print(f"El area del triangulo es: {resultado:.2f}")

        elif opcion == "0":
            print("Saliendo de la calculadora...")
            break

        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
