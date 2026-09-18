#HUMBERTO ZAMORA MOSCOSO-61549938
def resta(a, b):
    return a - b


def suma(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def validar(operacion):
    if operacion not in ["+", "-", "", "/"]:
        raise ValueError("Operación no válida.")


def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación a realizar (+, -,, /): ").strip()
        validar(operacion)

        if operacion == "+":
            resultado = suma(a, b)
        elif operacion == "-":
            resultado = resta(a, b)
        elif operacion == "*":
            resultado = multiplicar(a, b)
        elif operacion == "/":
            resultado = dividir(a, b)

    except ValueError as e:
        print("Error:", e)

    else:
        print("El resultado de la operación es:", resultado)
    finally:
        print("Gracias por usar la calculadora.")


main()