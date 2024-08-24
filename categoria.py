class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

def registrar_categoria():
    nombre = input("Nombre de la categoría: ")
    descripcion = input("Descripción de la categoría: ")
    categoria = Categoria(nombre, descripcion)
    print(f"Categoría registrada: {categoria.nombre}, {categoria.descripcion}")
if __name__ == "__main__":
    registrar_categoria()
