# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de 
# multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(num):
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} * {i} = {resultado}")

# Programa Principal

numero = int(input("Por favor, ingresá un número entero: "))

tabla_multiplicar(numero)