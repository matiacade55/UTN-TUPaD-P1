#FUNCIONES DE ORDENAMIENTO

def bubble_sort(lista,key): # key indica al algoritmo por cuál clave ordenar
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j][key] > lista[j + 1][key]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista # Retorna la lista ordenada

def quick_sort(lista, key):
    # caso base
    if len(lista) <= 1:
        return lista
    
    # paso recursivo
    pivote = lista.pop() # Usamos el último elemento como pivote

    # Creamos listas vacías
    lista1 = []
    lista2 = []

    for e in lista: # Se recorre c/ elemento de la lista
        # Se indica tanto al elemento como al pivote cuál es la clave del diccionario a considerar
        if e[key] <= pivote[key]: 
            lista1.append(e) # Se agrega el elemento a la lista1
        else:
            lista2.append(e) # Se agrega el elemento a la lista2
    
    lista1 = quick_sort(lista1, key) # Se aplica recursividad en ambas listas
    lista2 = quick_sort(lista2, key)

    return lista1 + [pivote] + lista2 # pivote se concatena como una lista de un elemento