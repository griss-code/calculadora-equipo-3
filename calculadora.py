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
    # TODO (Miembro 2)
    pass


def division(a, b):
    # TODO (Miembro 2)
    pass


def mostrar_resultados(operacion, resultado):
    # TODO (Líder)
    pass


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
        r = division(a, b)
    else:
        print("Operación no válida")
        return
    mostrar_resultados(op, r)


if __name__ == "__main__":
    main()