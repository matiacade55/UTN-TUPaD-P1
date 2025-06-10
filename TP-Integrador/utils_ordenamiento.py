from utils_tiempo import medir_tiempo_promedio
from utils_formato_salidas import mostrar_lista_ordenada
import random

#FUNCIONES DE ORDENAMIENTO

def ordenamiento_general(nombre_ordenamiento, funcion_ordenamiento, lista, clave):
    print(f"{nombre_ordenamiento}")

    # Medimos el tiempo tiempo
    tiempo = medir_tiempo_promedio(lambda: funcion_ordenamiento(lista, clave))

    # Ordenamos y mostramos primeros productos
    lista_ordenada = funcion_ordenamiento(lista, clave)
    mostrar_lista_ordenada(lista_ordenada)

    print(f"Tiempo promedio: {tiempo:.6f} ms\n")

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
    '''
    mitad = len(lista) // 2 Se utilizó para representar el mejor caso.
    pivote = lista[mitad]
    
    pivote = lista[-1] # Utilizado para representar el peor caso.
    '''
    pivote = random.choice(lista)
    # Creamos listas vacías
    lista1 = []
    lista2 = []

    for e in lista[:-1]: # Se recorre c/ elemento de la lista
        # Se indica tanto al elemento como al pivote cuál es la clave del diccionario a considerar
        if e[key] <= pivote[key]: 
            lista1.append(e) # Se agrega el elemento a la lista1
        else:
            lista2.append(e) # Se agrega el elemento a la lista2
    
    lista1 = quick_sort(lista1, key) # Se aplica recursividad en ambas listas
    lista2 = quick_sort(lista2, key)

    return lista1 + [pivote] + lista2 # pivote se concatena como una lista de un elemento