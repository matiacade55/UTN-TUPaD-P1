'''
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
'''
for i in range(101):
    print(i)

'''
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
'''
num = int(input("Por favor, ingresá un número entero: "))
cont = 0

while num != 0:
    
    num = num // 10
    cont += 1
    

print(cont)

'''
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
'''
num1 = int(input("Por favor ingresa el primer numero: "))
num2 = int(input("Porfavor ingresa el segundo numero: "))
suma = 0

#Fuerzo que el mas bajo sea el inicio del for y el mas alto el fin 
inicio = min(num1, num2) + 1
fin = max(num1, num2)

for i in range (inicio, fin):
    suma += i

print(suma)

'''
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
'''
num = int(input("Por favor ingrese el nº a sumar o 0 (cero) para detener el programa: "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Por favor ingrese el nº a sumar o 0 (cero) para detener el programa: "))

if suma != 0:
    print(f"La suma de los números ingresados es: {suma}.")
else:
    print("El programa se detuvo al inicio, no se ingresaron números a sumar.")

'''
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
'''
from random import randint

num = int(input("Adivina! Del 0 al 9, en que número estoy pensado?: "))
num_aleatorio = randint(0,9)

while num != num_aleatorio:
    num = int(input("Erraste! Volvé a intentar. Del 0 al 9, en que número estoy pensado?: "))

print(f"Felicitaciones! Adivinaste. El número que estaba pensado era el {num_aleatorio}")

'''
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
'''
for i in range(98, 1, -2):
    print(i)

'''
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
'''
num = int(input("Por favor, ingresá un numero entero positivo: "))
suma = 0

while num <= 0:
    print("Error! El número ingresado debe ser mayor que 0 (cero).")
    num = int(input("Por favor, ingresá un numero entero positivo: "))

for i in range(num):
    suma += i

print(f"La suma de todos los números comprendidos entre 0 y {num} es: {suma}")

'''
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
'''
cant_num = 100

cant_positivo = 0
cant_negativo = 0
cant_par = 0
cant_impar = 0

for i in range(cant_num):
    num = int(input(f"Por favor ingresa el {i+1}º número: "))
    if num >= 0:
        cant_positivo += 1
    else:
        cant_negativo += 1
    if num % 2 == 0:
        cant_par += 1
    else:
        cant_impar += 1

print(f"Positivos: {cant_positivo}, Negativos: {cant_negativo}, Pares: {cant_par}, Impares: {cant_impar}")

'''
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
'''
cant_num = 100
suma = 0

for i in range(cant_num):
    num = int(input(f"Por favor, ingresá el {i+1}º número"))
    suma = suma + num

print(f"El promedio de los número ingresados es {suma / cant_num}")

'''
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
'''
from math import trunc

num = int(input("Por favor, ingresá un número de dos o mas dígitos: "))
digito = 0
inverso = 0

while num != 0:
    digito = num % 10
    num = trunc(num/10)
    inverso = inverso * 10 + digito

print(f"El inverso del número ingresado es {inverso}")