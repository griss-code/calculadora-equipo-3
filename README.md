# calculadora-equipo-3
Equipo creado para subir el código de la calculadora.

Se creó una calculadora sencilla hecha en Python para practicar el flujo con Git y Github.

Los integrantes:
1. Grissel (Líder) se encargó de la función mostrarResultados y el manejo de la división por cero
2. Luis Daniel (miembro 1) se encargó de la función obtenerNumeros para la suma y la resta
3. Jorge (miembro 2) se encargó de la función Operaciones para la multiplicación y división


3. Se creo el archivo calculadora.py con un código base, de manera que cada función se separó y el líder de equipo asignó su parte a cada integrante para evitar conflictos.
    
4. Ese código base se subió a main
C:\Users\Griss\calculadora-equipo-3>git add calculadora.py
C:\Users\Griss\calculadora-equipo-3>git commit -m "Agregar el código para seguirlo como base para la calculadora"
C:\Users\Griss\calculadora-equipo-3>git push origin main

5. Posteriormente se agregó a Jorge y a Daniel
7. Se protegió la rama main
8. Se completó la función de suma y resta por Daniel
9. Se completaron las funciones de multiplicación de División por Jorge
10. Posteriormente, se aceptaron sus pull requests y se hizo un merge por cada uno, una vez que se revisaron sus cambios
11. Por último se completó la función de obtener resultado y también se agregó un try catch en la división

## Funciones

- `obtener_numeros()`: le pide dos números al usuario y los valida.
- `suma(a, b)`, `resta(a, b)`, `multiplicacion(a, b)`, `division(a, b)`: son las operaciones básicas de suma, resta, multiplicación y división.
- `mostrar_resultados(operacion, resultado)`: simplemente imprime la operación y el resultado.
- `main()`: es el que controla el flujo del programa.