# Nombre: operaciones.py
# Objetivo: mostrar como trabajan los métodos o funciones en python
# Autor: Diego Aaron Figueroa Campos
# Fecha: 29 de junio de 2019

#-----------------------------------
# Función para sumar dos numeros
#-----------------------------------
def suma(num1,num2):
    return num1+num2
    
#-----------------------------------
# Función para restar dos numeros
#-----------------------------------
def resta(num1,num2):
    return num1-num2
	
#-----------------------------------
# Función para multiplicar dos numeros
#-----------------------------------
def multiplicacion(num1,num2):
    return num1*num2
	
#-----------------------------------
# Función para dividir dos numeros
#-----------------------------------
def division(num1,num2):
    return num1/num2
    
#-----------------------------------
# Función para comparar dos numeros
#-----------------------------------
def compara(num1,num2):
    if(num1>num2):
        print("El mayor es: ", num1)
      
    elif(num1<num2):
        print("El mayor es: ", num2)
        
    else:
        print("Los 2 números son iguales")

#-----------------------------------
# Función para hacer un ciclo con for
#-----------------------------------
def cuenta(num1,num2):
    if(num1<num2):
        for i in range(num1,num2+1):
            print("Contador: ", i)
    else:
        for i in range(num1,num2-1,-1):
            print("Contador: ", i)

#Función main
def main():
    ciclo = True
    while (ciclo == True):
        print("---Operaciones Básicas con Enteros--")
        print("\n")
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        #Invocamos las funciones
        print("La suma es: " + str(suma(num1,num2)))
        print("La resta es: " + str(resta(num1,num2)))
        print("La multiplicación es: " + str(multiplicacion(num1,num2)))
        print("La división es: " + str(division(num1,num2)))
        compara(num1,num2)
        cuenta(num1,num2)
        
        cad = input("¿Desea hacer otro cálculo (s/n)? : ")
        if(cad == "S" or cad == "s"):
            ciclo = True
        else:
            ciclo = False
            
#inicia programa principal
if __name__ == "__main__" :
    main()

