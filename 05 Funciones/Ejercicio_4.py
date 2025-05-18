# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área 
#   del círculo. calcular_perimetro_ circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#   Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Importo pi para que el valor sea exacto
from math import pi

def calcular_area_circulo(rad):
    area = pi * (rad**2)
    return area

def calcular_perimetro_circulo(rad):
    perimetro = 2 * pi * rad
    return perimetro

# Programa Principal

radio = float(input("Por favor, ingresá el radio de la circunferencia: "))

# Asigno el valor del retorno de las funciones a las dos variables, para luego mostrarlas con un print
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es {area} y su perímetro es: {perimetro}")