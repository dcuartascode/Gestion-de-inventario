import tkinter as tk
from tkinter import simpledialog, messagebox

class Producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria

    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            messagebox.showinfo("Stock actualizado", f"Se han agregado {cantidad} unidades. Stock actual: {self.stock}")
        else:
            messagebox.showerror("Error", "La cantidad a agregar debe ser mayor que 0.")

    def retirar_stock(self, cantidad):
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
            messagebox.showinfo("Stock actualizado", f"Se han retirado {cantidad} unidades. Stock actual: {self.stock}")
        elif cantidad > self.stock:
            messagebox.showerror("Error", "No hay suficiente stock para retirar esa cantidad.")
        else:
            messagebox.showerror("Error", "La cantidad a retirar debe ser mayor que 0.")

def registrar_producto():
    nombre = simpledialog.askstring("Registro de Producto", "Nombre del producto:")
    descripcion = simpledialog.askstring("Registro de Producto", "Descripción del producto:")
    precio = simpledialog.askfloat("Registro de Producto", "Precio del producto:")
    stock_inicial = simpledialog.askinteger("Registro de Producto", "Stock inicial del producto:")
    categoria = simpledialog.askstring("Registro de Producto", "Categoría del producto:")

    if nombre and descripcion and precio is not None and stock_inicial is not None and categoria:
        producto = Producto(nombre, descripcion, precio, stock_inicial, categoria)
        messagebox.showinfo("Producto registrado", f"Producto registrado: {producto.nombre}, {producto.descripcion}, ${producto.precio}, Stock: {producto.stock}, Categoría: {producto.categoria}")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
