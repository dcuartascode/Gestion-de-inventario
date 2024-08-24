class producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria
        self.proveedores = []

    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"Se han agregado {cantidad} unidades al stock. Stock actual: {self.stock}")
        else:
            print("La cantidad a agregar debe ser mayor que 0.")

    def retirar_stock(self, cantidad):
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se han retirado {cantidad} unidades del stock. Stock actual: {self.stock}")
        elif cantidad > self.stock:
            print("No hay suficiente stock para retirar esa cantidad.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    def calcular_valor_total(self):
        valor_total = self.precio * self.stock
        print(f"El valor total de los productos en stock es: ${valor_total:.2f}")
        return valor_total

def registrar_producto():
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    precio = float(input("Precio del producto: "))
    stock_inicial = int(input("Stock inicial del producto: "))
    categoria = input("Categoría del producto: ")
    return producto(nombre, descripcion, precio, stock_inicial, categoria)

if __name__ == "__main__":
    producto = registrar_producto()  

    while True:
        opcion = input("¿Deseas agregar, retirar stock o calcular el valor total? (a/r/c/n): ").lower()
        if opcion == 'a':
            cantidad = int(input("Cantidad de stock a agregar: "))
            producto.agregar_stock(cantidad)
        elif opcion == 'r':
            cantidad = int(input("Cantidad de stock a retirar: "))
            producto.retirar_stock(cantidad)
        elif opcion == 'c':
            producto.calcular_valor_total()
        elif opcion == 'n':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")