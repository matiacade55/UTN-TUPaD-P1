# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):

    if len(palabra) <= 1: # Cuando la palabra tenga una letra devuelve True. Si se llego a una es porque se fue recortando, porque es palindromo.
        return True
    elif palabra[0] != palabra[-1]: # Si la primer letra es distinta de la ultima ya no es palindromo.
        return False
    
    return es_palindromo(palabra[1:-1]) # Es -1 porque no lo incluye

print(es_palindromo("anana"))