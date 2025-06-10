from utils_tiempo import medir_tiempo_promedio
from utils_formato_salidas import mostrar_producto

#FUNCIONES DE BUSQUEDA

def busqueda_general(nombre_busqueda, funcion_busqueda, lista, nombre_producto):
    print(f"{nombre_busqueda}")

    if funcion_busqueda.__name__ == "buscar_por_nombre_binaria": # Si es búsqueda binaria ordenamos la lista
        lista = sorted(lista, key=clave_ordenamiento)

    resultado = funcion_busqueda(lista, nombre_producto) # Buscarmos el producto
    mostrar_producto(resultado) # Lo mostramos formateado

    tiempo = medir_tiempo_promedio(lambda: funcion_busqueda(lista, nombre_producto)) # Medición del tiempo promedio
    print(f"Tiempo promedio: {tiempo:.6f} ms\n")
    

def buscar_por_nombre_lineal(lista, nombre):

    for producto in lista:

        # Si el valor de la clave "nombre" == nombre(ingresado por el usuario)
        if producto["nombre"] == nombre:
            return producto
    
    return None

def clave_ordenamiento(producto):
    return producto["nombre"] # Le indica a sorted() por cuál clave debe ordenar

def buscar_por_nombre_binaria(lista, nombre):

    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2 # Encontramos el punto medio de la lista
        nombre_medio = lista[medio]["nombre"] # Obtenemos el nombre del producto que esta en el medio.
        nombre_buscado = nombre

        if nombre_medio == nombre_buscado:
            return lista[medio] # Devuelve el producto encontrado en la posición medio
        elif nombre_medio < nombre_buscado:
            inicio = medio + 1 # Corremos el inicio hacia la derecha (el buscado esta en la mitad de la derecha)
        else:
            final = medio - 1 # Corremos el final hacia la izquierda (el buscado esta en la mitad de la izquierda)
    
    return None