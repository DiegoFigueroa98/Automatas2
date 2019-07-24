#------------------------------------------------------------------
# Nombre: leerEnsamblador.py
# Objetivo: leer un texto y generar código ensamblador
# Autor: Diego Aaron Figueroa Campos
# Fecha: 23/07/2019
#------------------------------------------------------------------

#Librerías importadas
import os

# Abre archivo en modo lectura
archivo = open('codigo.txt','r')  

def leerArchivo():
    archivo = open('codigo.txt','r')
    cadena = archivo.read()
    archivo.close()
    return cadena

def crearArchivo():
    file = open("codigoEnsamblador.txt", "w")
    file.write("MOV AH,02" + os.linesep)
    file.write("MOV DX,0000" + os.linesep)
    file.write("INT 10")
    file.close()
    print("\nArchivo creado exitosamente...")

def analizarArchivo():
    cadena = leerArchivo()
    if cadena == "cls":
        print("\nInstrucción identificada correctamente...")
        crearArchivo()
    else:
        print("\nError, instrucción no identificada...")

# Prueba de ingreso
def main():
    analizarArchivo()

# Inicia programa principal
if __name__ == "__main__" :
    main()
