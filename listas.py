# Nombre: listas.py
# Objetivo: mostrar el funcionamiento delas listas en python
# Autor: Diego Aaron Figueroa Campos
# Fecha: 01 de julio de 2019

# Librerías
import os

# Variables globales
lista = []

#--------------------------------------------------------------------
# Función para agregar items a la lista
#--------------------------------------------------------------------

def agregarItem(dato):
    lista.append(dato)

#--------------------------------------------------------------------
# Función para buscar un item en la lista
#--------------------------------------------------------------------

def buscarItem(dato):
    if dato in lista:
        print("\nItem encontrado...")
    else:
        print("\nEse Item no existe en la lista...")

#--------------------------------------------------------------------
# Función para agregar items a la lista
#--------------------------------------------------------------------

def agregarItem(dato):
    lista.append(dato)

#--------------------------------------------------------------------
# Función para borrar items a la lista
#--------------------------------------------------------------------

def eliminarItem(dato):
    # Validar si el elemento está en la lista
    if dato in lista:
        lista.remove(dato)
        print("\nItem eliminado...")
    else:
        print("\nEse Item no existe en la lista...")

#--------------------------------------------------------------------
# Función para imprimir los elementos de la lista
#--------------------------------------------------------------------

def imprimirLista():
    for i, valor in enumerate(lista):
        print(str(i) + " - "+ valor)

# Función principal
def main():
    ciclo = True
    while ciclo == True:
        print("\n--- Script para trabajar con listas ---")
        print("\n1.- Agregar elementos a la lista")
        print("2.- Buscar un elemento en la lista ")
        print("3.- Modificar un elemento en la lista")
        print("4.- Eliminar un elemento de la lista")
        print("5.- Imprime los elementos de la lista")
        print("6.- Salir")

        opc = int(input("\nElija una opción entre 1 y 6: "))

        if(opc == 1):
            item = input("\nIntroduce valor del elemento: ")
            agregarItem(item)
            lista.
        elif(opc == 2):
            print("")
        elif(opc == 3):
            print("")
        elif(opc == 4):
            print("")
        elif(opc == 5):
            print("")
        elif(opc == 6):
            ciclo = False
            print("\n*** Fin del programa ***")
        else:
            print("\nSelecciona un entero entre 1 y 6")
        #Borrar pantalla
        os.system ("cls") 

#Inicia programa principal
if __name__ == "__main__" :
    main()