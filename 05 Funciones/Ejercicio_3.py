# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedirlos datos al usuario y llamar a esta función con los 
# valores ingresados.

def informacion_personal(nom, ape, edad, residencia):
    print(f"Soy {nom} {ape}, tengo {edad} años y vivo en {residencia}")

# Programa Principal

nombre = input("Por favor, ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("Ingresá tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)