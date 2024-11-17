import tkinter as tk
from tkinter import simpledialog, messagebox

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

def registrar_categoria():
    nombre = simpledialog.askstring("Registro de Categoría", "Nombre de la categoría:")
    if nombre:
        categoria = Categoria(nombre)
        messagebox.showinfo("Categoría registrada", f"Categoría registrada: {categoria.nombre}")
    else:
        messagebox.showerror("Error", "El nombre de la categoría no puede estar vacío.")
