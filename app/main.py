while True:
        print("Registro de Entidades")
        print("")
        print("1. Registrar Producto")
        print("2. Registrar Categoría")
        print("3. Registrar Proveedor")
        print("4. Registrar Bodega")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            from app.producto import registrar_producto
            registrar_producto()
        elif opcion == '2':
            from app.categoria import registrar_categoria
            registrar_categoria()
        elif opcion == '3':
            from app.proveedor import registrar_proveedor
            registrar_proveedor()
        elif opcion == '4':
            from bodega import registrar_bodega
            registrar_bodega()
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intente de nuevo.")