class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

def registrar_categoria():
    nombre = input("Nombre de la categoría: ")
    return Categoria(nombre)

if __name__ == "__main__":
    categorias = []
    productos = []

    while True:
        opcion = input("¿Deseas registrar una categoría o un producto? (c/p/n): ").lower()
        if opcion == 'c':
            categoria = registrar_categoria()
            categorias.append(categoria)
        elif opcion == 'p':
            if not categorias:
                print("Primero debes registrar al menos una categoría.")
            else:
                print("Categorías disponibles:")
                for i, cat in enumerate(categorias):
                    print(f"{i + 1}. {cat.nombre}")
                cat_index = int(input("Selecciona el número de la categoría para el producto: ")) - 1
                categoria_seleccionada = categorias[cat_index]
                from producto import registrar_producto
                registrar_producto()
        elif opcion == 'n':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

