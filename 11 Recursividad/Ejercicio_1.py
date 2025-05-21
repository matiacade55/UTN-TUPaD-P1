# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular 
# y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)

num = int(input("Por favor ingresa el número entero: "))

for num in range(1, num + 1):
    print(f"El factorial del número {num} es: {factorial_recursivo(num)}")

