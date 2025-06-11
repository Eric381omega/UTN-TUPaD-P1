#Nombre: Eric Suarez Dubs

#Actividades:

#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:

#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:

#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios

precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.

#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe

contactos = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i + 1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre que querés buscar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró un contacto con el nombre '{consulta}'.")

#5) Solicita al usuario una frase e imprime:

#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j + 1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:

#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Ana", "Luis", "Marta", "Jorge"}
parcial2 = {"Luis", "Sofía", "Marta", "Carlos"}

ambos = parcial1 & parcial2

solo_uno = parcial1 ^ parcial2

al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock = {
    "manzanas": 10,
    "bananas": 5,
    "pan": 20
}

producto = input("Ingresá el nombre del producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input(f"¿Cuántas unidades querés agregar a {producto}?: "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingresá stock inicial para agregarlo: "))
    stock[producto] = nuevo_stock
    print(f"{producto} agregado con stock: {stock[producto]}")

print("\nStock actualizado:")
for prod, cantidad in stock.items():
    print(f"{prod}: {cantidad}")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {}

for i in range(3):
    dia = input(f"Ingresá el día del evento {i + 1}: ")
    hora = input(f"Ingresá la hora del evento {i + 1} (formato 00:00): ")
    evento = input(f"Ingresá la descripción del evento {i + 1}: ")
    agenda[(dia, hora)] = evento

print("\nAgenda cargada:")
for clave, valor in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {valor}")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:

#• Las capitales sean las claves.
#• Los países sean los valores.

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)

