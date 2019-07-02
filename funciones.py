#-*-coding:utf8;-*-
#qpy:3
#qpy:console
# Nombre: funciones.py
# Objetivo: muestra como trabajan los métodos o funciones en python
# Autor: Diego Aaron Figueroa Campos
# Fecha: 29 de junio de 2019

def mensaje():
    print("Hola guapa")
    nombre = input("Ingrese su nombre: ")
    print(f"Te odio {nombre}")

def main():
    mensaje()
    
#inicia programa principal
if __name__ == "__main__" :
    main()
