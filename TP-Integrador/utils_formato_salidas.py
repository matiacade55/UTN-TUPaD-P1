# Formateo de salidas

def mostrar_producto(producto):
    if producto:
        print(f"Id: {producto['id']} - Nombre: {producto['nombre']} - Precio: ${producto['precio']} - Vencimiento: {producto['vencimiento']}")
    elif producto == None:
        print("Producto no encontrado")

def mostrar_lista_ordenada(lista_ordenada):
    for producto in lista_ordenada:
        mostrar_producto(producto)