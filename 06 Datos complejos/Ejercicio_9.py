# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

# Creo una agenda con algunos eventos de ejemplo
agenda = {
    ("lunes", "10:00"): "Reunión con el equipo",
    ("martes", "14:00"): "Clase de programación",
    ("miércoles", "09:00"): "Consulta médica"
}

# Pido al usuario que consulte un día y hora
dia = input("Ingresá un día: ").lower()
hora = input("Ingresá una hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada en ese horario.")
