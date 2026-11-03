# calculadora.py - Calculadora en línea de comandos


def obtener_numeros():
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        return a, b
    except ValueError:
        print("Error: Debes ingresar números válidos.")
        exit()


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


def mostrar_resultados(operacion, resultado):
    print(f"\nOperación: {operacion}")
    print(f"Resultado: {resultado}")


def main():
    print("=== Calculadora ===")
    a, b = obtener_numeros()
    op = input("Operación (+, -, *, /): ")
    if op == "+":
        r = suma(a, b)
    elif op == "-":
        r = resta(a, b)
    elif op == "*":
        r = multiplicacion(a, b)
    elif op == "/":
        try:
            r = division(a, b)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return
    else:
        print("Operación no válida")
        return
    mostrar_resultados(op, r)


if __name__ == "__main__":
    main()
