# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques 
# que necesita para construir toda la pirámide.

# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n_bloques):
    if n_bloques == 1:
        return 1
    
    return n_bloques + contar_bloques(n_bloques - 1)

cant_bloques = 10
total_bloques = contar_bloques(cant_bloques)

print(f"La cantidad de bloques necesarios para construir una pirámide de {cant_bloques} bloques de base es: {total_bloques}")