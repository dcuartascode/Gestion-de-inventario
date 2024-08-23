class Producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria
        self.proveedores = []


    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    precio = float(input("Precio del producto: "))
    stock_inicial = int(input("Stock inicial del producto: "))
    categoria = input("Categoría del producto: ")
