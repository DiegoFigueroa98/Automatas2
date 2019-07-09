#------------------------------------------------------------------
# Nombre: calculadora_Visual.py
# Objetivo: simular una calculadora básica
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------

# Script para simular una calculadora básica

import tkinter as tk
from tkinter import *



# Función para sumar 
def sumar():
    # Recuperamos los datos de los campos de texto
    num1 = txtC1.get()
    num2 = txtC2.get()
    print("La suma es: ", int(num1)+ int(num2))

# Función para restar
def restar():
    num1 = txtC1.get()
    num2 = txtC2.get()
    print("La resta es: ", int(num1) - int(num2))

# Función para multiplicar
def multiplicar():
    num1 = txtC1.get()
    num2 = txtC2.get()
    print("La multiplicación es: ", int(num1) * int(num2))

# Función para dividir
def dividir():
    num1 = txtC1.get()
    num2 = txtC2.get()
    print("La división es: ", int(num1) / int(num2))




# Funcion para salir de la app
def salir():
    wv.destroy()


# Programa principal 

# Creamos las ventana
wv = tk.Tk()
# Modificamos el tamaño de la ventana
wv.geometry("500x400")
# Titulo de la ventana
wv.title("Operaciones Básicas")

# Creamos la etiqueta
l1 = Label(None, text="Número uno:")
l2 = Label(None, text="Número dos: ")

#Creamos los botones
bs = Button(None, text='Sumar', command=sumar)
br = Button(None, text='Restar', command=restar)
bm = Button(None, text='Multiplicar', command=multiplicar)
bd = Button(None, text='Dividir', command=dividir)
bq = Button(None, text= 'Salir', command=salir)

# creamos los campos de texto
txtC1 = Entry(wv)
txtC2 = Entry(wv)

# Alineamos los widgets
l1.grid(row=1, column=10)
l2.grid(row=2, column=10)
# campos de texto
txtC1.grid(row = 1, column=15)
txtC2.grid(row = 2, column= 15)
# Botones
bs.grid(row = 4, column=5)
br.grid(row = 4, column=10)
bm.grid(row = 4, column=15)
bd.grid(row = 4, column=20)
bq.grid(row = 4, column=35)


# Ciclo de espera de eventos
wv.mainloop()