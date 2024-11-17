import tkinter as tk
from tkinter import simpledialog, messagebox

class Proveedor:
    def __init__(self, nombre, direccion, telefono, productos):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos

def registrar_proveedor():
    nombre = simpledialog.askstring("Registro de Proveedor", "Nombre del proveedor:")
    direccion = simpledialog.askstring("Registro de Proveedor", "Dirección del proveedor:")
    telefono = simpledialog.askstring("Registro de Proveedor", "Teléfono del proveedor:")
    productos = simpledialog.askstring("Registro de Proveedor", "Lista de productos (separados por coma):").split(',')

    if nombre and direccion and telefono and productos:
        proveedor = Proveedor(nombre, direccion, telefono, productos)
        messagebox.showinfo("Proveedor registrado", f"Proveedor registrado: {proveedor.nombre}, {proveedor.direccion}, {proveedor.telefono}, Productos: {', '.join(proveedor.productos)}")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
