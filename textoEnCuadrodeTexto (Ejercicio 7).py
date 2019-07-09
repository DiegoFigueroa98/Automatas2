#------------------------------------------------------------------
# Nombre: textoEnCuadrodeTexto.py
# Objetivo: probar los cuadros de texto con botones
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------

import tkinter as tk
from tkinter import *

# Función para sumar 
def trans():
    # Recuperamos los datos de los campos de texto
    txtC1.set("Hola mundo peludo")

# Función para borrar la caja de texto
def borrar():
    txtC1.set("")

# Función para salir de la app
def salir():
    wv.destroy()

# Programa principal 

# Creamos las ventana
wv = tk.Tk()
wv.config(bd=15)

# Modificamos el tamaño de la ventana
wv.geometry("400x400")

# Titulo de la ventana
wv.title("Probando los cuadros de texto")

# Creamos la etiqueta
l1 = Label(wv, text="Ingresa un texto: ")

# creamos los campos de texto
txtC1 = StringVar()

Entry(wv, justify="left",textvariable=txtC1,state="disabled").pack()

#Creamos los botones
bt = Button(wv, text="Mostrar", command=trans).pack(side="left")
bb = Button(wv, text="Borrar", command=borrar).pack(side="left")
bs = Button(wv, text="Salir", command=salir).pack(side="left")

# Ciclo de espera de eventos
wv.mainloop()