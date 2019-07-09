#------------------------------------------------------------------
# Nombre: sueldoTrabajadores.py
# Objetivo: capturar el sueldo de 10 trabajadores
# calcular el total de la nómina
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------

def main():
    suma = 0.0
    for i in range (1,11):
        sueldo = float(input("Ingrese el sueldo del trabajador %d: "%i))
        suma += sueldo
    print("\nEl total de la nomina es: ",suma)
    
if __name__ == "__main__":
    main()
