class Proveedor:
    def __init__(self, nombre, direccion, telefono, productos):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos
        
def registrar_proveedor():
    nombre = input("Nombre del proveedor: ")
    direccion = input("Dirección del proveedor: ")
    telefono = input("Teléfono del proveedor: ")
    productos = input("Lista de productos que suministra (separados por comas): ").split(',')
    proveedor = Proveedor(nombre, direccion, telefono, productos)
    print(f"Proveedor registrado: {proveedor.nombre}, {proveedor.direccion}, {proveedor.telefono}, {proveedor.productos}")
if __name__ == "__main__":
    registrar_proveedor()