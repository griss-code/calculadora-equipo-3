# calculadora.py - Calculadora en línea de comandos


def obtener_numeros():
    # TODO (Miembro 1)
    pass


def suma(a, b):
    # TODO (Miembro 1)
    pass


def resta(a, b):
    # TODO (Miembro 1)
    pass


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


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
