# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#    Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio 

# Programa Principal

a = int(input("Por favor, ingresá el primer número: "))
b = int(input("Por favor, ingresá el segundo número: "))
c = int(input("Por favor, ingresá el tercer número: "))

print(f"El promedio de los números ingresados es: {calcular_promedio(a, b, c)}")