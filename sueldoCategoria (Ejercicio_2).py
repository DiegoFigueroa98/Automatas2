#------------------------------------------------------------------
# Nombre: sueldoCategoria.py
# Objetivo: capturar el sueldo y la categoría y calcula
# el sueldo de un trabajador, calcular el aumento correspondiente
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------


def main():
    print("\nCategoría 1 : Aumento 15%")
    print("Categoría 2 : Aumento 10%")
    print("Categoría 3 : Aumento 8%")
    print("Categoría 4 : Aumento 7%")
    cat = int(input("\nIngrese su categoría: "))
    sueldo = float(input("Ingrese su sueldo: "))
    if (cat == 1):
        sueldo *= 1.15
    elif (cat == 2):
        sueldo *= 1.10
    elif (cat == 3):
        sueldo *= 1.08
    elif (cat == 4):
        sueldo *= 1.07
    print("\nEl sueldo final es: ",sueldo)
    
if __name__ == "__main__":
    main()