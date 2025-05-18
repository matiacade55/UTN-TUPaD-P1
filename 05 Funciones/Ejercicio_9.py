# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#    Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_farenheit(celsius):
    temperatura_farenheit = (celsius * 9 / 5) + 32
    return temperatura_farenheit

# Programa Principal

temp_celsius = float(input("Por favor, ingresá la temperatura en ºC: "))

print(f"La temperatura ingresada equivale a {celsius_a_farenheit(temp_celsius)}ºF")
