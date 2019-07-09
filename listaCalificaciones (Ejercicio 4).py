#------------------------------------------------------------------
# Nombre: listaCalificaciones.py
# Objetivo: capturar lista de calificaciones de N alumnos
# El promedio general de alumnos
# Numero de alumnos aprobados y número de alumnos reprobados
# Porcentaje de alumnos aprobados y reprobados
# Número de alumnos cuya calificación fue mayor a 80
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------

def main():
    alumnos = []
    suma = 0.0
    apro = 0
    rep = 0
    mayor = 0
    
    ciclo = True
    while ciclo == True:
        nota = float(input("Introduce calificación: "))
        alumnos.append(nota)
        if (nota > 70):
            apro += 1
            if (nota >80):
                mayor +=1
        else:
            rep += 1
        suma += nota
        
        resp = input("\nDesea capturar otra calificación (s/n)?: ")
    
        if(resp == "S" or resp == "s"):
            ciclo = True
        elif(resp == "N" or resp == "n"):
            ciclo = False
        
    print("\n**********************************************************")
    print("\nPromedio general: ",suma/len(alumnos))
    print("\nAlumnos aprobados: ",apro)
    print("\nAlumnos reprobados: ",rep)
    print("\nPorcentaje de alumnos aprobados: ",(apro*100)/len(alumnos),"%")
    print("\nPorcentaje de alumnos reprobados: ",(rep*100)/len(alumnos),"%")
    print("\nNúmero de alumnos con calificación mayor a 80: ",mayor)
    print("\n**********************************************************")
    
    
if __name__ == "__main__":
    main()