"1 Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,"
" deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. "

edad = int(input("Introduce tu edad: "))

if edad >=18:
    print ("es mayor de edad.")
else:
     print ("es menor de edad.")

"2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá"
"mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el"
"mensaje “Desaprobado”."

nota = int(input("Introduzca su nota: "))

if nota >=6:
    print ("Aprobado.")
else:
     print ("Desaprobado.")

"3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un"
"número par, imprimir por en pantalla el mensaje Ha ingresado un número par; en caso"
"contrario, imprimir por pantalla Por favor, ingrese un número par. Nota: investigar el uso del"
"operador de módulo (%) en Python para evaluar si un número es par o impar."

while True:
        numero = int(input("Ingrese un número par: "))
        if numero % 2 == 0:
            print("Ha ingresado un número par.")
            break
        else:
            print("Por favor, ingrese un número par.")

"4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las"
"siguientes categorías pertenece:"
"● Niño/a: menor de 12 años."
"● Adolescente: mayor o igual que 12 años y menor que 18 años."
"● Adulto/a joven: mayor o igual que 18 años y menor que 30 años."
"● Adulto/a: mayor o igual que 30 años."

anios = int(input("Introduzca su edad: "))

if anios <12:
     print ("eres un niño")
elif anios >=12 and anios <18:
     print("eres un adolescente")
elif anios >=18 and anios <30:
     print("eres un joven")
elif anios >=30:
     print("eres un adulto")

"5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres"
"(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en"
"pantalla el mensaje Ha ingresado una contraseña correcta; en caso contrario, imprimir por"
"pantalla Por favor, ingrese una contraseña de entre 8 y 14 caracteres. Nota: investigue el uso"
"de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal"
"como una lista o un string."

while True:
    contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
    
    if 8 <= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta.")
        break
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

"6)escribir un programa que tome la lista"
"numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si"
"hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."
"Definir la lista numeros_aleatorios de la siguiente forma:"

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media_valor = mean(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)
moda_valor = mode(numeros_aleatorios)

print("Números aleatorios:", numeros_aleatorios)
print(f"Media: {media_valor}")
print(f"Mediana: {mediana_valor}")
print(f"Moda: {moda_valor}")

if media_valor > mediana_valor > moda_valor:
    print("Distribución con sesgo positivo (a la derecha).")
elif media_valor < mediana_valor < moda_valor:
    print("Distribución con sesgo negativo (a la izquierda).")
elif media_valor == mediana_valor == moda_valor:
    print("Distribución sin sesgo.")
else:
    print("No se puede determinar un sesgo claro.")

"7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado"
"termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por"
"pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por"
"pantalla."

frase = input("Ingrese una palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
    
print("Su palabra es :", frase)

"8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3"
"dependiendo de la opción que desee:"
"1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO."
"2. Si quiere su nombre en minúsculas. Por ejemplo: pedro."
"3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."
"El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el"
"usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),"
"lower() y title() de Python para convertir entre mayúsculas y minúsculas."

nombre = input("Ingrese su nombre: ")

print("Elija una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")

opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida. Por favor ingrese 1, 2 o 3.")

"9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:"
"● Menor que 3: Muy leve (imperceptible)."
"● Mayor o igual que 3 y menor que 4: Leve (ligeramente perceptible)."
"● Mayor o igual que 4 y menor que 5: Moderado (sentido por personas, pero generalmente no causa daños)."
"● Mayor o igual que 5 y menor que 6: Fuerte (puede causar daños en estructuras débiles)."
"● Mayor o igual que 6 y menor que 7: Muy Fuerte (puede causar daños significativos)."
"● Mayor o igual que 7: Extremo (puede causar graves daños a gran escala)."

try:
    magnitud = float(input("Ingrese la magnitud del terremoto: "))

    if magnitud < 3:
        print("Muy leve (imperceptible).")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible).")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños).")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles).")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos).")
    else:  # magnitud >= 7
        print("Extremo (puede causar graves daños a gran escala).")

except ValueError:
    print("Por favor, ingrese un número válido.")

"10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año"
"Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes"
"del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla"
"si el usuario se encuentra en otoño, invierno, primavera o verano"

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper()
mes = input("Ingrese el mes actual (ejemplo: enero, febrero, etc.): ").strip().lower()
dia = int(input("Ingrese el día del mes actual: "))

estaciones_norte = {
    "invierno": [("diciembre", 21, 31), ("enero", 1, 31), ("febrero", 1, 28), ("marzo", 1, 20)],
    "primavera": [("marzo", 21, 31), ("abril", 1, 30), ("mayo", 1, 31), ("junio", 1, 20)],
    "verano": [("junio", 21, 30), ("julio", 1, 31), ("agosto", 1, 31), ("septiembre", 1, 20)],
    "otoño": [("septiembre", 21, 30), ("octubre", 1, 31), ("noviembre", 1, 30), ("diciembre", 1, 20)]
}

estaciones_sur = {
    "verano": estaciones_norte["invierno"],
    "otoño": estaciones_norte["primavera"],
    "invierno": estaciones_norte["verano"],
    "primavera": estaciones_norte["otoño"]
}

def obtener_estacion(mes, dia, estaciones):
    for estacion, periodos in estaciones.items():
        for periodo in periodos:
            if periodo[0] == mes and periodo[1] <= dia <= periodo[2]:
                return estacion
    return None

if hemisferio == "N":
    estacion = obtener_estacion(mes, dia, estaciones_norte)
elif hemisferio == "S":
    estacion = obtener_estacion(mes, dia, estaciones_sur)
else:
    estacion = None
    
if estacion:
    print(f"La estación actual en su hemisferio es: {estacion.capitalize()}")
else:
    print("Entrada no válida. Verifique los datos ingresados.")
