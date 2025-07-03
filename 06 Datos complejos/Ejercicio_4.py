# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

nombre = ""
num_tel = ""

contactos = {}

for i in range(0,3):

    opcion = input("Querés agregar un nuevo contacto? S/N: ")

    if opcion == "S" or opcion == "s":
        nombre = input("Nombre: ")
        num_tel = input("Número: ")

        contactos[nombre] = num_tel
    else:
        print("Adiós!")
        exit()

print(contactos)

# Consultar contacto

contacto_buscado = input("Ingrsá el nombre del contacto a consultar: ")

if contacto_buscado in contactos:
    print(f"El número de {contacto_buscado} es: {contactos[contacto_buscado]}")
else:
    print("El contacto no existe")