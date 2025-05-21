# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
num = int(input("Elige la posición de la la serie de Fibonaccio que quieras conocer: "))

for num in range(num + 1):
    print(fibonacci_recursivo(num))