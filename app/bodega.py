import tkinter as tk
from tkinter import simpledialog

class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima, productos):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = productos

def registrar_bodega():
    nombre = simpledialog.askstring("Registro de Bodega", "Nombre de la bodega:")
    ubicacion = simpledialog.askstring("Registro de Bodega", "Ubicación de la bodega:")
    capacidad_maxima = int(simpledialog.askstring("Registro de Bodega", "Capacidad máxima de la bodega:"))
    productos = simpledialog.askstring("Registro de Bodega", "Lista de productos (separados por coma):").split(',')
    bodega = Bodega(nombre, ubicacion, capacidad_maxima, productos)
    tk.messagebox.showinfo("Bodega registrada", f"{bodega.nombre}, {bodega.ubicacion}, {bodega.capacidad_maxima}, {bodega.productos}")
