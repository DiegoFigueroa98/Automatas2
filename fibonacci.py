# Nombre: fibonacci.py
# Objetivo: obtener la serie fibonacci
# Autor: Diego Aaron Figueroa Campos
# Fecha: 01 de julio de 2019

#--------------------------------------------------------------------
# Función para calcular la serie de fibonacci
#--------------------------------------------------------------------
def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        c = b+a
        a = b
        b = c
        
    return a

# Función principal
def main():
    print("\n -- Script para identificar la serie de fibonacci")
    num = int(input("\nIntroduce la longitud que tendrá la serie: "))
    print("\n*** Serie de fibonacci ***")
    for i in range(num):
        print(fibonacci(i))
    print("\n*** Fin de la serie ***")
 
#Inicia programa principal
if __name__ == "__main__" :
    main()