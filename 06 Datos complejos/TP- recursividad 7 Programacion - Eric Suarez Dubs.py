"TP prgramacion"

"Nombre: Eric Suarez Dubs"

"1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros"
"entre 1 y el número que indique el usuario"

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Introduce un número entero positivo: "))

if num < 1:
    print("Por favor, introduce un número mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {num}:")
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")

"2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Introduce una posición entera no negativa para la serie de Fibonacci: "))

if pos < 0:
    print("Por favor, introduce un número entero no negativo.")
else:
    print(f"Serie de Fibonacci hasta la posición {pos}:")
    for i in range(pos + 1):
        print(f"F({i}) = {fibonacci(i)}")

"3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1) . Prueba esta función en un algoritmo general."

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente (entero no negativo): "))

if exponente < 0:
    print("Este programa solo acepta exponentes enteros no negativos.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")

"4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto."
"Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este procedimiento:"

"1. Dividir el número por 2."
"2. Guardar el resto (0 o 1)."
"3. Repetir el proceso con el cociente hasta que llegue a 0."
"4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario."

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Introduce un número entero positivo: "))

if numero < 0:
    print("Por favor, introduce un número entero positivo.")
elif numero == 0:
    print("El número binario de 0 es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"La representación binaria de {numero} es: {binario}")

"5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es."

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Introduce una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')

"6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos."

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234))  
print(suma_digitos(9))     
print(suma_digitos(305))   

"7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque."
"Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide."

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

entrada = input("Introduce el número de bloques en el nivel más bajo (entero positivo): ")

if entrada.isdigit() and int(entrada) >= 1:
    numero = int(entrada)
    total = contar_bloques(numero)
    print(f"Para construir la pirámide con {numero} bloques en la base, se necesitan {total} bloques en total.")
else:
    print("Entrada inválida. Debes ingresar un número entero positivo mayor o igual a 1.")

"8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número."

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

entrada_num = input("Introduce un número entero positivo: ")
entrada_dig = input("Introduce el dígito que quieres contar (0-9): ")

if entrada_num.isdigit() and entrada_dig.isdigit():
    numero = int(entrada_num)
    digito = int(entrada_dig)

    if 0 <= digito <= 9:
        resultado = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
    else:
        print("El dígito debe estar entre 0 y 9.")
else:
    print("Entrada inválida. Ambos valores deben ser enteros positivos.")
