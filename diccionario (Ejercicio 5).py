#------------------------------------------------------------------
# Nombre: diccionario.py
# Objetivo: capturar los datos generales de un alumno del ITC
# imprimir los datos y modificar al menos uno de los datos
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------

def main():
    ciclo = True
    while ciclo == True:
        print("*****************************************")
        print("1.- Registrar datos del alumno")
        print("2.- Imprimir datos del alumno ")
        print("3.- Modificar un dato del alumno")
        print("4.- Salir")
        print("*****************************************")

        opc = int(input("\nElija una opción entre 1 y 4: "))

        if(opc == 1):
            nombre = input("\nIngrese el nombre completo del alumno: ")
            fecha = input("\nIngrese la fecha de nacimiento: ")
            carrera = input("\nIngrese la carrera a la que pertenece: ")
            prom = input("\nIngrese el promedio general: ")
            datos_alumno = {
            "Nombre completo":nombre,
            "Fecha de nacimiento":fecha,
            "Carrera profesional":carrera,
            "Promedio":prom,
            }
            
        elif(opc == 2):
            print("\n**** Datos del alumno ****")
            for clave, valor in datos_alumno.items():
                print(clave + ": " + valor)
            
        elif(opc == 3):
            print("\n1.-Nombre completo")
            print("2.-Fecha de nacimiento ")
            print("3.-Carrera")
            print("4.-Promedio general")
            opc = int(input("\nElija el dato a modificar entre 1 y 4: "))
            if(opc == 1):
                nombre = input("\nIngrese el nuevo nombre completo: ")
                datos_alumno['Nombre Completo']=nombre
            elif(opc == 2):
                fecha = input("\nIngrese la nueva fecha de nacimiento: ")
                datos_alumno['Fecha de nacimiento']=fecha
            elif(opc == 3):
                carrera = input("\nIngrese la nueva carrera: ")
                datos_alumno['Carrera profesional']=carrera
            elif(opc == 4):
                prom = input("\nIngrese el nuevo promedio general: ")
                datos_alumno['Promedio']=prom

        elif(opc == 4):
            ciclo = False
            print("\n*** Fin del programa ***")
        else:
            print("\nSelecciona un entero entre 1 y 6")
    
if __name__ == "__main__":
    main()
