# Nombre: circunferencia.py
# Objetivo: calcular el área de diámetro de una circunferencia e importar la librería math
# Autor: Diego Aaron Figueroa Campos
# Fecha: 01 de julio de 2019

import math as mat
import os

#--------------------------------------------------------------------
# Función para calcular el área
#--------------------------------------------------------------------

def calcularArea(r):
    area = mat.pi*(pow(r,2))
    return area

#--------------------------------------------------------------------
# Función para calcular el área
#--------------------------------------------------------------------

def calcularDiametro(d):
    diam = d * 2
    return diam

def main():
    ciclo = True
    while ciclo == True:
        print("\n -- Script para Calcular el Área de una Circunferencia")
        radio = float(input("\nIntroduce el valor del radio: "))

        #Invocar un método
        print("El área es: ",str(calcularArea(radio)))
        print("El diametro es: ",str(calcularDiametro(radio)))

        resp = input("\n¿Desea hacer otro cálculo (s/n)? : ")
        if(resp == "S" or resp == "s"):
            ciclo = True
            #Borrar pantalla
            os.system ("cls") 
        else:
            ciclo = False
    else:
        print("\n*** Fin del programa ***")

#Inicia programa principal
if __name__ == "__main__" :
    main()
