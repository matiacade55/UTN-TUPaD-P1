# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):

    nombre = input(f"Nombre del alumno {i+1}: ")
    
    print("Ingresá las 3 notas:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    # Guardo la tupla como valor para cada clave 'nombre'
    alumnos[nombre] = (nota1, nota2, nota3)

# Mostrar promedios
print("Promedios de los alumnos:")

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")
