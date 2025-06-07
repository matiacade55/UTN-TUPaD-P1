#FUNCIONES DE ORDENAMIENTO

def bubble_sort(lista,key):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j][key] > lista[j + 1][key]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

def quick_sort(lista, key):
    # caso base
    if len(lista) <= 1:
        return lista
    
    # paso recursivo
    pivote = lista.pop() # Usamos el último elemento como pivote
    lista1 = []
    lista2 = []

    for e in lista:
        if e[key] <= pivote[key]:
            lista1.append(e)
        else:
            lista2.append(e)
    
    lista1 = quick_sort(lista1, key)
    lista2 = quick_sort(lista2, key)

    return lista1 + [pivote] + lista2 # pivote se concatena como una lista de un elemento