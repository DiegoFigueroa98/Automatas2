# Nombre: conexionMySQL.py
# Objetivo: mostrar el funcionamiento de Python con MySQL
# Autor: Diego Aaron Figueroa Campos
# Fecha: 14 de julio de 2019

import pymysql

def conexion():
    try:
        global conexion
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='automatasii')
        print("Conexión correcta")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

def agregar(clave, nombre):
    try:
        cursor = conexion.cursor()
        consulta = "INSERT INTO keyword(clave, nombre) VALUES (%s, %s);"
        cursor.execute(consulta, (clave, nombre))
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def mostrar():
    try:
        print("\n*** Mostrando los datos ***\n")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM keyword;")
        keywords = cursor.fetchall()
        for keyword in keywords:
            print(keyword)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def modificar(clave, nombre):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM keyword WHERE clave = %s;",(clave))
        numFilas = cursor.rowcount
        if numFilas == 0:
            print ("\nError: no existe un dato con la clave",clave)
        else:
            cursor.execute("UPDATE keyword SET nombre = %s WHERE clave = %s;",(nombre,clave))
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def eliminar(clave):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM keyword WHERE clave = %s;",(clave))
        numFilas = cursor.rowcount
        if numFilas == 0:
            print ("\nError: no existe un dato con la clave",clave)
        else:
            cursor.execute("DELETE FROM keyword WHERE clave = %s;",(clave))
        conexion.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

# Función principal
def main():
    conexion()
    ciclo = True
    while ciclo == True:
        print("\n--- Script para trabajar con base de datos MySQL ---")
        print("\n1.- Agregar datos")
        print("2.- Mostrar datos ")
        print("3.- Modificar un dato")
        print("4.- Eliminar un dato")
        print("5.- Salir")

        opc = int(input("\nElija una opción entre 1 y 5: "))

        if(opc == 1):
            clave = int(input("\nIngrese una clave: "))
            nombre = input("\nIngrese un nombre: ")
            agregar(clave, nombre)
        elif(opc == 2):
            mostrar()
        elif(opc == 3):
            clave = int(input("\nIntroduce la clave del dato a modificar: "))
            nombre = input("\nIngrese el nuevo nombre: ")
            modificar(clave,nombre)
        elif(opc == 4):
            clave = int(input("\nIntroduce la clave del dato a eliminar: "))
            eliminar(clave)
        elif(opc == 5):
            ciclo = False
            print("\n*** Fin del programa ***")
        else:
            print("\nSelecciona un entero entre 1 y 5")

#Inicia programa principal
if __name__ == "__main__" :
    main()


