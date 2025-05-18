# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#   de horas correspondientes. Solicitar al usuario los segundos y mostrar
#   el resultado usando esta función.

def segundos_a_horas(seg):
    horas = seg / 3600
    return horas

# Programa Principal

segundos = float(input("Por favor, ingresa la cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print(f"La cantidad de segundos ingresados equivalen a {horas} horas.")