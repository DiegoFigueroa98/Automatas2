# Nombre: factorial.py
# Objetivo: obtener el factorial de un número
# Autor: Diego Aaron Figueroa Campos
# Fecha: 01 de julio de 2019

#--------------------------------------------------------------------
# Función para obtener el factorial de un número
#--------------------------------------------------------------------
def factorial(num):
    res = 1
    while num > 1:
        res *= num
        num -= 1
    return res

# Función principal
def main():
    print("\n -- Script para identificar obtener el factorial")
    num = int(input("\nIntroduce un número: "))
    print("\nEl factorial de",str(num),"es:",factorial(num))
 
#Inicia programa principal
if __name__ == "__main__" :
    main()