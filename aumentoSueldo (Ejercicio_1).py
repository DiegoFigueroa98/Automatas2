#------------------------------------------------------------------
# Nombre: aumentoSueldo.py
# Objetivo: tomar como dato el sueldo de un trabajador y aplicar un
# aumento del 15% si su sueldo es inferior a $1000.00 y del 12% en caso contrario
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------

def main():
    sueldo = float(input("Ingrese su sueldo: "))
    if (sueldo < 1000):
        sueldo *= 1.15
    else:
        sueldo *= 1.12
        
    print("\nEl sueldo final es: ",sueldo)
    
if __name__ == "__main__":
    main()