import tkinter as tk
from tkinter import messagebox
from bodega import registrar_bodega
from categoria import registrar_categoria
from producto import registrar_producto
from proveedor import registrar_proveedor

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario")
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.root, text="SISTEMA DE INVENTARIO", font=("Arial", 14)).pack(pady=10)
        
        opciones = [("Registrar Bodega", registrar_bodega), 
                    ("Registrar Categoría", registrar_categoria), 
                    ("Registrar Producto", registrar_producto), 
                    ("Registrar Proveedor", registrar_proveedor)]
        
        for texto, comando in opciones:
            tk.Button(self.root, text=texto, command=comando, width=20).pack(pady=5)
        
        tk.Button(self.root, text="Salir", command=self.root.quit, width=20).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
