#FUNCIONES DE BUSQUEDA

def buscar_por_nombre_lineal(lista, nombre):

    for producto in lista:

        if producto["nombre"] == nombre:
            return producto
    
    return None

def clave_ordenamiento(lista):
    return lista["nombre"]

def buscar_por_nombre_binario(lista, nombre):

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