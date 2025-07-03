# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

# Separo la frase en palabras
palabras = frase.split()

# Set guarda las palabras sin repetir
palabras_unicas = set(palabras)

# Creo un diccionario con los conteos
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# Mostrar los resultados
print(f"Palabras únicas: {palabras_unicas}")

print(f"Conteo de cada palabra: {conteo_palabras}")

