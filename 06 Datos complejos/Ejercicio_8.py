# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock = {
    "aspirina": 10,
    "paracetamol": 20,
    "ibuprofeno": 15
}

producto = input("Ingresá el nombre del producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]} unidades.")

    agregar = input("¿Querés agregar unidades? (S/N): ").lower()
    if agregar == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    print("Producto no encontrado.")
    nuevo = input("¿Querés agregar este producto? (S/N): ").lower()
    if nuevo == "s":
        unidades = int(input("¿Cuántas unidades tiene?: "))
        stock[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")

# Mostrar el stock actualizado
print("\nStock actualizado:")
print(stock)
