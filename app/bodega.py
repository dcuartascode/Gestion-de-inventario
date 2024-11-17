class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima, productos):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = productos

def registrar_bodega():
    nombre = input("Nombre de la bodega: ")
    ubicacion = input("Ubicación de la bodega: ")
    capacidad_maxima = int(input("Capacidad máxima de la bodega: "))
    productos = input("Lista de productos almacenados: ").split(',')
    bodega = Bodega(nombre, ubicacion, capacidad_maxima, productos)
    print(f"Bodega registrada: {bodega.nombre}, {bodega.ubicacion}, {bodega.capacidad_maxima}, {bodega.productos}")

if __name__ == "__main__":
 registrar_bodega()