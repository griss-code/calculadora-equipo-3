# calculadora-equipo-3
Equipo creado para subir el código de la calculadora

A continuación, vamos a explicar lo realizado para esta actividad.

1. Se creó el repositorio en GitHub con el nombre calculadora-equipo-3, se marcó como Public, se agregó un README.md y se le dio clic en Create repository.
   
2. Posteriormente se clono y se creó el código base:
C:\Users\Griss>git clone https://github.com/griss-code/calculadora-equipo-3.git
C:\Users\Griss>cd calculadora-equipo-3

3. Se creo el archivo calculadora.py con el siguiente contenido, de manera que cada función se separó y el líder de equipo asignó su parte a cada integrante para evitar conflictos:
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
    
5. Este código base se subió a main
C:\Users\Griss\calculadora-equipo-3>git add calculadora.py
C:\Users\Griss\calculadora-equipo-3>git commit -m "Agregar el código para seguirlo como base para la calculadora"
C:\Users\Griss\calculadora-equipo-3>git push origin main

7. Posteriormente se agregó a Jorge y a Daniel
8. [Me falta seguir escribiendo los demás pasos]
