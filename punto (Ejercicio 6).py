#------------------------------------------------------------------
# Nombre: punto.py
# Objetivo: muestra el manejo de clases en python
# Autor: Diego Aaron Figueroa Campos
# Fecha: 04/07/2019
#------------------------------------------------------------------

#Librerías importadas
import math as mat

class Punto(object):
    #Constructor de la clase
    def __init__(self, valorX, valorY):
        self.x = valorX
        self.y = valorY

    #Métodos get
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #Métodos set
    def setX(self, valorX):
        self.x = valorX
    
    def setY(self, valorY):
        self.y = valorY

    #Métodos alternos
    def toString(self):
        return "\nEl punto tiene las siguientes coordenadas: "+str(self.x)+","+str(self.y)

#Creación clase circunferencia
class Circunferencia(Punto):
    def __init__(self, valorX, valorY, valorRadio):
        self.x = valorX
        self.y = valorY
        self.radio = valorRadio

    def getRadio(self):
        return self.radio

    def getArea(self):
        return mat.pi * mat.pow(self.radio,2)
    
    def setRadio(self, valorRadio):
        self.radio = valorRadio

    def toString(self):
        return "\nLa circunferencia tiene como centro: "+str(self.getX())+","+str(self.getY())+","+str(self.radio)+"\nTiene como área: "+str(self.getArea())

class Cilindro(Circunferencia):
    def __init__(self, valorX, valorY, valorRadio, valorAltura):
        self.x = valorX
        self.y = valorY
        self.radio = valorRadio
        self.altura = valorAltura

    def getAltura(self):
        return self.altura

    def getVolumen(self):
        return self.getArea()*self.altura
    
    def setAltura(self, valorAltura):
        self.altura = valorAltura

    def toString(self):
        return "\nEl cilindro X: "+str(self.getX())+", Y: "+str(self.getY())+", Radio: "+str(self.getRadio())+", Altura: "+str(self.getAltura())+"\nTiene como área: "+str(self.getArea())+"\nTiene como volumen: "+str(self.getVolumen())

def main():
    #Creamos el objeto p1
    p1 = Punto(2,3)
    #Invocamos el método toString
    print(p1.toString())

    #Creamos el objeto p2
    p2 = Punto(0,0)
    #Invocamos el método set
    p2.setX(-2)
    p2.setY(-4)
    print(p2.toString())

    #Creamos el p3
    p3 = Circunferencia(-2,-4,12.34)
    #Invocamos el método set
    p3.setX(-2)
    p3.setY(-4)
    print(p3.toString())

    #Creamos el p4
    p4 = Cilindro(-2,-4,5.5,8)
    #Invocamos el método set
    p4.setX(2)
    p4.setY(4)
    print(p4.toString())
    
if __name__ == "__main__":
    main()
