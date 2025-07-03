# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# Diccionario original: país → capital
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín"
}

# Invierto claves y valores: capital → país
capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

# Muestro el nuevo diccionario
print("Diccionario invertido (capital → país):")
print(capitales_paises)
