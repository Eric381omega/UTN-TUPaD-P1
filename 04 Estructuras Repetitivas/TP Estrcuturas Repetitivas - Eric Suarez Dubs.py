'Nombre: Eric Suarez Dubs'

"1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea en Python"

for i in range(101):
    print(i)

"2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene."

numero = input("Introduce un número entero: ")

cantidad_digitos = len(numero) if numero.isdigit() else len(numero) - 1

print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

"3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores."

valor1 = int(input("Introduce el primer valor: "))
valor2 = int(input("Introduce el segundo valor: "))

if valor1 > valor2:
    valor1, valor2 = valor2, valor1  

suma = sum(range(valor1 + 1, valor2))

print(f"La suma de los números entre {valor1} y {valor2} (excluyendo esos dos valores) es: {suma}")

"4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0."

total = 0

while True:
    numero = int(input("Introduce un número entero (ingresa 0 para terminar): "))
    
    if numero == 0:
        break
    
    total += numero

print(f"El total acumulado es: {total}")

"5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número."

import random

numero_aleatorio = random.randint(0, 9)

intentos = 0

while True:

    intento = int(input("Adivina el número entre 0 y 9: "))
    
    intentos += 1
    
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_aleatorio:
        print("El número es mayor, intenta nuevamente.")
    else:
        print("El número es menor, intenta nuevamente.")

"6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente."

for i in range(100, -1, -2):
    print(i)

"7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario."

n = int(input("Introduce un número entero positivo: "))

if n < 0:
    print("Por favor, introduce un número positivo.")
else:
    suma = sum(range(n + 1))
    
    print(f"La suma de los números entre 0 y {n} es: {suma}")

"8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos."

cantidad_numeros = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad_numeros):
    while True:
        entrada = input(f"Introduce el número {i + 1}: ")
        if entrada.strip() == "":
            print("No ingresaste ningún número. Intenta de nuevo.")
            continue
        try:
            numero = int(entrada)
            break  
        except ValueError:
            print("Entrada no válida. Debes ingresar un número entero.")

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResumen:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

"9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores."

cantidad_numeros = 100

suma = 0

for i in range(cantidad_numeros):
    while True:
        entrada = input(f"Introduce el número {i + 1}: ")
        if entrada.strip() == "":
            print("No ingresaste ningún número. Intentá de nuevo.")
            continue
        try:
            numero = int(entrada)
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresá un número entero.")
    
    suma += numero

media = suma / cantidad_numeros

print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

"10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."

numero = input("Introduce un número entero: ")

if numero.startswith("-"):
    numero_invertido = "-" + numero[:0:-1]  
else:
    numero_invertido = numero[::-1]

print(f"El número invertido es: {numero_invertido}")
