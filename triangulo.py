# Nombre: triangulo.py
# Objetivo: identificar el tipo de triángulo de acuerdo al valor de sus lados
# Autor: Diego Aaron Figueroa Campos
# Fecha: 01 de julio de 2019

import os

#--------------------------------------------------------------------
# Función identificar el tipo de triángulo
#--------------------------------------------------------------------

def identificarTriangulo(l1,l2,l3):
    if(l1==l2 and l2==l3):
       print("\nEl triángulo es equilatero: ",l1,", ",l2,", ",l3)
    elif(l1==l2 or l1==l3 or l2==l3):
       print("\nEl triángulo es isósceles: ",l1,", ",l2,", ",l3)
    elif (l1!=l2 and l1!=l3 and l2!=l3):
       print("\nEl triángulo es escaleno: ",l1,", ",l2,", ",l3)

    print("\nEl perímetro del triángulo es: ",(l1+l2+l3))

def main():
    ciclo = True
    while ciclo == True:
        print("\n -- Script para identificar triángulos")
        lado1 = float(input("\nIntroduce el lado 1: "))
        lado2 = float(input("Introduce el lado 2: "))
        lado3 = float(input("Introduce el lado 3: "))
        #Invocar un método
        identificarTriangulo(lado1,lado2,lado3)

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
