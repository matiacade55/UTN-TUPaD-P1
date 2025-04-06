'''1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
'''

edad = int(input("Por favor, ingresá tu edad: "))

if edad > 18:
    print("Es mayor de edad")

'''
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar 
por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
'''
nota = float(input("Por favor, ingresá tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

'''
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir 
por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
'''
numero = int(input("Por favor, ingresá un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

'''
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años.
'''
edad = int(input("Por favor, ingresá tu edad: "))

if edad >= 0 and edad < 12:
    print("Sos Niño/a")
elif edad >= 12 and edad < 18:
    print("Sos Adolescente")
elif edad >= 18 and edad < 30:
    print("Sos Adulto/a joven")
elif edad >= 30:
    print("Sos Adulto/a")
else:
    print("La edad ingresada no es válida")

'''
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa 
una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, 
imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() 
en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
'''
contra = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")
long_contra = len(contra)

if long_contra >= 8 and long_contra <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

'''
6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números.
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal 
a partir del siguiente criterio:  
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.  
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.  
● Sin sesgo: cuando la media, la mediana y la moda son iguales.  

Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare 
para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
'''
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Media = {media}, Mediana = {mediana}, Moda = {moda}")

#sesgo positivo o a la derecha
if media > mediana and mediana > moda:
    print("Sesgo positivo")
#sesgo negativo o a la izquierda    
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
#sin sesgo
elif media == mediana == moda:
    print("Sin sesgo")

'''
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final
e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
'''
frase = input("Por favor, ingresá una palabra o una frase: ")

#Accedo a la ultima letra de la frase
ultima_letra = (frase[len(frase)-1]).lower()

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    frase = f"{frase}!"

print(frase)

'''
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:  
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.  
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.  
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.  

El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
Nota: investigue uso de las funciones   upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
'''
nombre = input("Por favor, ingresá tu nombre: ")
opcion = int(input("Por favor, seleccioná una opción:\n"
"1. Quiero mi nombre en mayúsculas\n"
"2. Quiero mi nombre en minúsculas\n"
"3. Quiero mi nombre con la primer letra mayúscula"))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("La opción seleccionada no es válida")

'''
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala 
de Richter e imprima el resultado por pantalla:  
● Menor que 3: "Muy leve" (imperceptible).  
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).  
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).  
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).  
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).  
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
'''
magnitud = float(input("Por favor, ingresá la magnitud del terremoto: "))
mensaje = ""

if magnitud > 0:
    if magnitud < 3:
        mensaje = "Muy Leve (imperceptible)"
    elif magnitud >= 3 and magnitud < 4:
        mensaje = "Leve (ligeramente perceptible)"
    elif magnitud >= 4 and magnitud < 5:
        mensaje = "Moderado (sentido por personas, pero generalmente no causa daños)"
    elif magnitud >= 5 and magnitud < 6:
        mensaje = "Fuerte (puede causar daños en estructuras débiles)"
    elif magnitud >= 6 and magnitud < 7:
        mensaje = "Muy fuerte (puede causar daños significativos)"
    else:
        mensaje = "Extremo (puede causar graves daños a gran escala)"
    
    print(f"La categoría del terremoto de magnitud {magnitud} en la escala de Richter es: {mensaje}")
else:
    print("Error: La magnitud debe ser mayor que cero")

'''
10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:  

- Periodo del año: Desde el 21 de diciembre hasta el 20 de marzo (incluidos)
    - Estación en el hemisferio norte: Invierno
    - Estación en el hemisferio sur: Verano  

- Desde el 21 de marzo hasta el 20 de junio (incluidos)
    - Estación en el hemisferio norte: Primavera
    - Estación en el hemisferio sur: Otoño   

- Desde el 21 de junio hasta el 20 de septiembre (incluidos)
    - Estación en el hemisferio norte: Verano
    - Estación en el hemisferio sur: Invierno  

- Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
    - Estación en el hemisferio norte: Otoño
    - Estación en el hemisferio sur: Primavera  

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
'''
hemisferio = (input("Por favor, ingresá el hemisfero en el que vives (N o S): ")).upper()
dia = int(input("Por favor, ingresá el dia a consultar: "))
mes = int(input("Por favor, ingresá el mes a consultar (nº de mes): "))

respuesta = ""

if dia > 0 and dia < 32:
    if mes > 0 and mes < 13:
            if hemisferio == "N" or hemisferio == "S":
                if (dia >= 21 and mes == 3) or (mes == 4 or mes == 5) or (dia <= 20 and mes == 6):
                    respuesta = "Primavera" if hemisferio == "N" else "Otoño"
                elif (dia >= 21 and mes == 6) or (mes == 7 or mes == 8) or (dia <=20 and mes == 9):
                    respuesta = "Verano" if hemisferio == "N" else "Invierno"
                elif (dia >= 21 and mes == 9) or (mes == 10 or mes == 11) or (dia <= 20 and mes == 12):
                    respuesta = "Otoño" if hemisferio == "N" else "Primavera"
                else:
                    respuesta = "Invierno" if hemisferio == "N" else "Verano"
            else:
                respuesta = "El hemisferio ingresado es incorrecto"
    else:
        respuesta = "El mes ingresado es incorrecto"
else:
    respuesta = "El dia ingresado es incorrecto"
            
print(respuesta)