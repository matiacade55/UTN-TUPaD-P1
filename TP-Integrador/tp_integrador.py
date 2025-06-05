
def buscar_por_nombre_lineal(lista, nombre):
    for producto in lista:
        if producto["nombre"].lower() == nombre.lower():
            return producto

    return None

def clave_ordenamiento(lista):
    return lista["nombre"].lower()

def buscar_por_nombre_binario(lista, nombre):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2 # Encontramos el punto medio de la lista
        nombre_medio = lista[medio]["nombre"].lower() # Obtenemos el nombre del producto que esta en el medio y lo pasamos a minúsculas
        nombre_buscado = nombre.lower()

        if nombre_medio == nombre_buscado:
            return lista[medio] # Devuelve el producto encontrado en la posición medio
        elif nombre_medio < nombre_buscado:
            inicio = medio + 1 # Corremos el inicio hacia la derecha (el buscado esta en la mitad de la derecha)
        else:
            final = medio - 1 # Corremos el final hacia la izquierda (el buscado esta en la mitad de la izquierda)
    
    return None


lista_productos_10 = [
    {"id": "0001", "nombre": "Aceite", "precio": 2500.00, "vencimiento": "2025-11-05"},
    {"id": "0002", "nombre": "Arroz", "precio": 1200.50, "vencimiento": "2026-01-15"},
    {"id": "0003", "nombre": "Leche", "precio": 1800.75, "vencimiento": "2025-11-20"},
    {"id": "0004", "nombre": "Pan", "precio": 900.25, "vencimiento": "2025-11-10"},
    {"id": "0005", "nombre": "Huevos", "precio": 2200.00, "vencimiento": "2025-12-01"},
    {"id": "0006", "nombre": "Azucar", "precio": 1500.90, "vencimiento": "2026-03-01"},
    {"id": "0007", "nombre": "Cafe", "precio": 3000.10, "vencimiento": "2026-04-25"},
    {"id": "0008", "nombre": "Fideos", "precio": 1100.80, "vencimiento": "2026-02-12"},
    {"id": "0009", "nombre": "Sal", "precio": 700.30, "vencimiento": "2026-05-30"},
    {"id": "0010", "nombre": "Harina", "precio": 1000.65, "vencimiento": "2026-05-01"}
]

lista_productos_100 = [
    {"id": "0001", "nombre": "Aceite", "precio": 2500.00, "vencimiento": "2025-11-05"},
    {"id": "0002", "nombre": "Arroz", "precio": 1200.50, "vencimiento": "2025-11-15"},
    {"id": "0003", "nombre": "Leche", "precio": 1800.75, "vencimiento": "2025-11-20"},
    {"id": "0004", "nombre": "Pan", "precio": 900.25, "vencimiento": "2025-11-25"},
    {"id": "0005", "nombre": "Huevos", "precio": 2200.00, "vencimiento": "2025-12-01"},
    {"id": "0006", "nombre": "Azucar", "precio": 1500.90, "vencimiento": "2025-12-05"},
    {"id": "0007", "nombre": "Cafe", "precio": 3000.10, "vencimiento": "2025-12-10"},
    {"id": "0008", "nombre": "Fideos", "precio": 1100.80, "vencimiento": "2025-12-15"},
    {"id": "0009", "nombre": "Sal", "precio": 700.30, "vencimiento": "2025-12-20"},
    {"id": "0010", "nombre": "Harina", "precio": 1000.65, "vencimiento": "2025-12-25"},
    {"id": "0011", "nombre": "Gaseosa", "precio": 1900.40, "vencimiento": "2026-01-01"},
    {"id": "0012", "nombre": "Jabon", "precio": 850.15, "vencimiento": "2026-01-05"},
    {"id": "0013", "nombre": "Pasta dental", "precio": 1300.20, "vencimiento": "2026-01-10"},
    {"id": "0014", "nombre": "Cereal", "precio": 2800.70, "vencimiento": "2026-01-15"},
    {"id": "0015", "nombre": "Galletas", "precio": 750.95, "vencimiento": "2026-01-20"},
    {"id": "0016", "nombre": "Tomate", "precio": 600.00, "vencimiento": "2026-01-25"},
    {"id": "0017", "nombre": "Papa", "precio": 550.00, "vencimiento": "2026-02-01"},
    {"id": "0018", "nombre": "Cebolla", "precio": 450.00, "vencimiento": "2026-02-05"},
    {"id": "0019", "nombre": "Zanahoria", "precio": 500.00, "vencimiento": "2026-02-10"},
    {"id": "0020", "nombre": "Manzana", "precio": 1200.00, "vencimiento": "2026-02-15"},
    {"id": "0021", "nombre": "Naranja", "precio": 1100.00, "vencimiento": "2026-02-20"},
    {"id": "0022", "nombre": "Banana", "precio": 1000.00, "vencimiento": "2026-02-25"},
    {"id": "0023", "nombre": "Pollo", "precio": 4500.00, "vencimiento": "2026-03-01"},
    {"id": "0024", "nombre": "Carne", "precio": 7000.00, "vencimiento": "2026-03-05"},
    {"id": "0025", "nombre": "Pescado", "precio": 5500.00, "vencimiento": "2026-03-10"},
    {"id": "0026", "nombre": "Queso", "precio": 3500.00, "vencimiento": "2026-03-15"},
    {"id": "0027", "nombre": "Manteca", "precio": 1600.00, "vencimiento": "2026-03-20"},
    {"id": "0028", "nombre": "Mermelada", "precio": 1400.00, "vencimiento": "2026-03-25"},
    {"id": "0029", "nombre": "Chocolate", "precio": 1700.00, "vencimiento": "2026-04-01"},
    {"id": "0030", "nombre": "Dulce de leche", "precio": 1900.00, "vencimiento": "2026-04-05"},
    {"id": "0031", "nombre": "Yogur", "precio": 950.00, "vencimiento": "2026-04-10"},
    {"id": "0032", "nombre": "Agua mineral", "precio": 700.00, "vencimiento": "2026-04-15"},
    {"id": "0033", "nombre": "Jugo", "precio": 1500.00, "vencimiento": "2026-04-20"},
    {"id": "0034", "nombre": "Cerveza", "precio": 1800.00, "vencimiento": "2026-04-25"},
    {"id": "0035", "nombre": "Vino", "precio": 3000.00, "vencimiento": "2026-05-01"},
    {"id": "0036", "nombre": "Detergente", "precio": 1200.00, "vencimiento": "2026-05-05"},
    {"id": "0037", "nombre": "Lavandina", "precio": 900.00, "vencimiento": "2026-05-10"},
    {"id": "0038", "nombre": "Escoba", "precio": 2000.00, "vencimiento": "2026-05-15"},
    {"id": "0039", "nombre": "Trapo", "precio": 500.00, "vencimiento": "2026-05-20"},
    {"id": "0040", "nombre": "Esponja", "precio": 300.00, "vencimiento": "2026-05-25"},
    {"id": "0041", "nombre": "Servilletas", "precio": 600.00, "vencimiento": "2026-06-01"},
    {"id": "0042", "nombre": "Papel higienico", "precio": 1400.00, "vencimiento": "2026-06-05"},
    {"id": "0043", "nombre": "Shampoo", "precio": 1800.00, "vencimiento": "2026-06-10"},
    {"id": "0044", "nombre": "Acondicionador", "precio": 1700.00, "vencimiento": "2026-06-15"},
    {"id": "0045", "nombre": "Jabon de tocador", "precio": 400.00, "vencimiento": "2026-06-20"},
    {"id": "0046", "nombre": "Crema de manos", "precio": 1100.00, "vencimiento": "2026-06-25"},
    {"id": "0047", "nombre": "Desodorante", "precio": 900.00, "vencimiento": "2026-07-01"},
    {"id": "0048", "nombre": "Enlatados", "precio": 800.00, "vencimiento": "2026-07-05"},
    {"id": "0049", "nombre": "Lentejas", "precio": 1000.00, "vencimiento": "2026-07-10"},
    {"id": "0050", "nombre": "Garbanzos", "precio": 950.00, "vencimiento": "2026-07-15"},
    {"id": "0051", "nombre": "Atun", "precio": 1300.00, "vencimiento": "2026-07-20"},
    {"id": "0052", "nombre": "Mayonesa", "precio": 850.00, "vencimiento": "2026-07-25"},
    {"id": "0053", "nombre": "Mostaza", "precio": 700.00, "vencimiento": "2026-08-01"},
    {"id": "0054", "nombre": "Ketchup", "precio": 900.00, "vencimiento": "2026-08-05"},
    {"id": "0055", "nombre": "Vinagre", "precio": 500.00, "vencimiento": "2026-08-10"},
    {"id": "0056", "nombre": "Especias", "precio": 600.00, "vencimiento": "2026-08-15"},
    {"id": "0057", "nombre": "Pimienta", "precio": 700.00, "vencimiento": "2026-08-20"},
    {"id": "0058", "nombre": "Oregano", "precio": 550.00, "vencimiento": "2026-08-25"},
    {"id": "0059", "nombre": "Comino", "precio": 580.00, "vencimiento": "2026-09-01"},
    {"id": "0060", "nombre": "Pimenton", "precio": 620.00, "vencimiento": "2026-09-05"},
    {"id": "0061", "nombre": "Extracto de tomate", "precio": 900.00, "vencimiento": "2026-09-10"},
    {"id": "0062", "nombre": "Caldo", "precio": 400.00, "vencimiento": "2026-09-15"},
    {"id": "0063", "nombre": "Salsa de soja", "precio": 1100.00, "vencimiento": "2026-09-20"},
    {"id": "0064", "nombre": "Aderezo", "precio": 800.00, "vencimiento": "2026-09-25"},
    {"id": "0065", "nombre": "Aceitunas", "precio": 1200.00, "vencimiento": "2026-10-01"},
    {"id": "0066", "nombre": "Pickles", "precio": 950.00, "vencimiento": "2026-10-05"},
    {"id": "0067", "nombre": "Choclo", "precio": 700.00, "vencimiento": "2026-10-10"},
    {"id": "0068", "nombre": "Arvejas", "precio": 650.00, "vencimiento": "2026-10-15"},
    {"id": "0069", "nombre": "Porotos", "precio": 800.00, "vencimiento": "2026-10-20"},
    {"id": "0070", "nombre": "Cerezas", "precio": 2500.00, "vencimiento": "2026-10-25"},
    {"id": "0071", "nombre": "Ciruelas", "precio": 1800.00, "vencimiento": "2026-11-01"},
    {"id": "0072", "nombre": "Duraznos", "precio": 2000.00, "vencimiento": "2026-11-05"},
    {"id": "0073", "nombre": "Peras", "precio": 1500.00, "vencimiento": "2026-11-10"},
    {"id": "0074", "nombre": "Uvas", "precio": 2200.00, "vencimiento": "2026-11-15"},
    {"id": "0075", "nombre": "Kiwi", "precio": 1700.00, "vencimiento": "2026-11-20"},
    {"id": "0076", "nombre": "Limon", "precio": 800.00, "vencimiento": "2026-11-25"},
    {"id": "0077", "nombre": "Lima", "precio": 900.00, "vencimiento": "2026-12-01"},
    {"id": "0078", "nombre": "Miel", "precio": 1600.00, "vencimiento": "2026-12-05"},
    {"id": "0079", "nombre": "Sopa", "precio": 750.00, "vencimiento": "2026-12-10"},
    {"id": "0080", "nombre": "Pure", "precio": 600.00, "vencimiento": "2026-12-15"},
    {"id": "0081", "nombre": "Gelatina", "precio": 500.00, "vencimiento": "2026-12-20"},
    {"id": "0082", "nombre": "Flan", "precio": 550.00, "vencimiento": "2026-12-25"},
    {"id": "0083", "nombre": "Helado", "precio": 2000.00, "vencimiento": "2027-01-01"},
    {"id": "0084", "nombre": "Alfajores", "precio": 1200.00, "vencimiento": "2027-01-05"},
    {"id": "0085", "nombre": "Budin", "precio": 1300.00, "vencimiento": "2027-01-10"},
    {"id": "0086", "nombre": "Magdalenas", "precio": 900.00, "vencimiento": "2027-01-15"},
    {"id": "0087", "nombre": "Snacks", "precio": 800.00, "vencimiento": "2027-01-20"},
    {"id": "0088", "nombre": "Papas fritas", "precio": 1100.00, "vencimiento": "2027-01-25"},
    {"id": "0089", "nombre": "Mani", "precio": 700.00, "vencimiento": "2027-02-01"},
    {"id": "0090", "nombre": "Pistachos", "precio": 2500.00, "vencimiento": "2027-02-05"},
    {"id": "0091", "nombre": "Almendras", "precio": 2200.00, "vencimiento": "2027-02-10"},
    {"id": "0092", "nombre": "Nueces", "precio": 2000.00, "vencimiento": "2027-02-15"},
    {"id": "0093", "nombre": "Pasas", "precio": 1500.00, "vencimiento": "2027-02-20"},
    {"id": "0094", "nombre": "Ciruelas pasas", "precio": 1400.00, "vencimiento": "2027-02-25"},
    {"id": "0095", "nombre": "Frutas secas", "precio": 1900.00, "vencimiento": "2027-03-01"},
    {"id": "0096", "nombre": "Semillas", "precio": 1000.00, "vencimiento": "2027-03-05"},
    {"id": "0097", "nombre": "Pescados enlatados", "precio": 1300.00, "vencimiento": "2027-03-10"},
    {"id": "0098", "nombre": "Vegetales congelados", "precio": 1500.00, "vencimiento": "2027-03-15"},
    {"id": "0099", "nombre": "Hamburguesas", "precio": 2800.00, "vencimiento": "2027-03-20"},
    {"id": "0100", "nombre": "Pizzas congeladas", "precio": 3000.00, "vencimiento": "2027-03-25"}
]

nombre_producto = input("Buscar producto por nombre: ").lower()

# Búsquedas lineales
resultado_de_10 = buscar_por_nombre_lineal(lista_productos_10, nombre_producto)
print("Búsqueda lineal entre 10 productos")
print(resultado_de_10)

resultado_de_100 = buscar_por_nombre_lineal(lista_productos_100, nombre_producto)
print("Búsqueda lineal entre 100 productos")
print(resultado_de_100)

# Búsquedas binarias (En este apartado se utiliza sorted() para ordenar ya que el objetivo es comparar solo los métodos de búsqueda)

lista_productos_10 = sorted(lista_productos_10, key=clave_ordenamiento) # Ordeno la lista de 10 productos por nombre.

resultado_de_10 = buscar_por_nombre_binario(lista_productos_10, nombre_producto)
print("Búsqueda binaria entre 10 productos")
print(resultado_de_10)

lista_productos_100 = sorted(lista_productos_100, key=clave_ordenamiento) # Ordeno la lista de 100 productos por nombre.

resultado_de_100 = buscar_por_nombre_binario(lista_productos_100, nombre_producto)
print("Búsqueda binaria entre 100 productos")
print(resultado_de_100)