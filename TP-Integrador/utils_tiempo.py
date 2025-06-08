import timeit

#FUNCIÓN PARA MEDIR TIEMPOS

def medir_tiempo_promedio(funcion, repeticiones=1000):
    
    tiempo_total = timeit.timeit(funcion, number=repeticiones)

    return (tiempo_total / repeticiones) * 1000  # Devuelve el tiempo promedio en ms