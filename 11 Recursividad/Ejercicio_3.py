# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
#    utilizando la fórmula 𝑛**𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia_recursiva(n, m):
    return n**m == n*n**(m-1)

print(potencia_recursiva(2,6))