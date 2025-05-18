# 7. Crear una función llamada operaciones_basicas(a, b) que reciba  dos números como parámetros y devuelva una tupla con el resultado
#    de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    resultados = (suma, resta, multiplicacion, division)

    return resultados

# Programa Principal

resultados = operaciones_basicas(10, 5)

print(f"Resultados de las operaciones realizadas con los números ingresados: \nSuma = {resultados[0]}, Resta = {resultados[1]}, Multiplicación = {resultados[2]}, División = {resultados[3]}")