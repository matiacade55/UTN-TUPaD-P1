# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {101,103,105,106}

# Convierto set a lista para poder recorrerlos
p_1 = list(parcial_1)
p_2 = list(parcial_2)

aprobo_ambos = []
for alumno in p_1:
    if alumno in p_1:
        if alumno in p_2:
            aprobo_ambos.append(alumno)

aprobo_uno = []
for alumno in p_1:
    if alumno not in p_2:
        aprobo_uno.append(alumno)

for alumno in p_2:
    if alumno not in p_1:
        aprobo_uno.append(alumno)


al_menos_uno = []
for alumno in p_1 + p_2:
    if alumno not in al_menos_uno:
        al_menos_uno.append(alumno)

print("Aprobaron ambos parciales:", aprobo_ambos)
print("Aprobaron solo uno:", aprobo_uno)
print("Aprobaron al menos uno:", al_menos_uno)