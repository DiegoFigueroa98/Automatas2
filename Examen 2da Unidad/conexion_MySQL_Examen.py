# Nombre: conexion_MySQL_Examen.py
# Objetivo: mostrar el funcionamiento de Python con MySQL de forma visual
# Autor: Diego Aaron Figueroa Campos
# Fecha: 16 de julio de 2019

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidget
from PyQt5.uic import loadUi
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import logoPrincipal_rc
import pymysql
import ast
import time

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('V_Principal.ui', self)
        self.btn_Agregar.clicked.connect(self.abrirVentanaAgregar)
        self.btn_Mostrar.clicked.connect(self.abrirVentanaMostrar)
        self.btn_Modificar.clicked.connect(self.abrirVentanaModificar)
        self.btn_Eliminar.clicked.connect(self.abrirVentanaEliminar)

    def abrirVentanaAgregar(self):
        self.hide()
        otraVentana = VentanaAgregar(self)
        otraVentana.show()

    def abrirVentanaMostrar(self):
        self.hide()
        otraVentana = VentanaMostrar(self)
        otraVentana.show()

    def abrirVentanaModificar(self):
        self.hide()
        otraVentana = VentanaModificar(self)
        otraVentana.show()

    def abrirVentanaEliminar(self):
        self.hide()
        otraVentana = VentanaEliminar(self)
        otraVentana.show()

class VentanaAgregar(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaAgregar, self).__init__(parent)
        loadUi('V_Agregar.ui', self)
        self.btn_Regresar.clicked.connect(self.abrirVentanaPrincipal)
        self.btn_Aceptar.clicked.connect(self.agregarDatos)
       
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def agregarDatos(self):
        try:
            clave = int(self.txt_Clave.toPlainText())
            nombre = (self.txt_Nombre.toPlainText())
            cursor = conexion.cursor()
            consulta = "INSERT INTO keyword(clave, nombre) VALUES (%s, %s);"
            cursor.execute(consulta, (clave, nombre))
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            dialogo = VentanaInformacion(self)
            dialogo.agregarTexto("Correcto\n\nKeyword agregada correctamente")
            dialogo.show()
            self.txt_Clave.setText("")
            self.txt_Nombre.setText("")

class VentanaMostrar(QMainWindow):

    def __init__(self, parent=None):
        super(VentanaMostrar, self).__init__(parent)
        loadUi('V_Mostrar.ui', self)
        self.btn_Aceptar.clicked.connect(self.cargarTabla)
        self.btn_Regresar.clicked.connect(self.abrirVentanaPrincipal)

    def cargarTabla(self):
        try:
            titulos = ["Clave","Nombre"]
            self.tb_Datos.setColumnCount(2)
            self.tb_Datos.setHorizontalHeaderLabels(titulos)
            self.tb_Datos.setColumnWidth(0,60)
            self.tb_Datos.setColumnWidth(1,259)

            cursor = conexion.cursor()
            filas = cursor.execute("SELECT * FROM keyword;")
            datos = cursor.fetchall()

            for filas in datos:
                self.agregarTabla(filas)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            dialogo = VentanaPregunta(self)
            dialogo.agregarTexto("Correcto\n\n¿Desea generar un PDF?")
            dialogo.show()

    def agregarTabla(self, columnas):
        posFila = self.tb_Datos.rowCount()
        self.tb_Datos.insertRow(posFila)

        for i, columna in enumerate(columnas):
            self.tb_Datos.setItem(posFila, i, QtWidgets.QTableWidgetItem(str(columna)))
        
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

class VentanaModificar(QMainWindow):

    def __init__(self, parent=None):
        super(VentanaModificar, self).__init__(parent)
        loadUi('V_Modificar.ui', self)
        self.btn_Regresar.clicked.connect(self.abrirVentanaPrincipal)
        self.btn_Aceptar.clicked.connect(self.modificarDatos)
        
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

    def modificarDatos(self):
        try:
            cursor = conexion.cursor()
            clave = int(self.txt_Clave.toPlainText())
            nombre = (self.txt_Nombre.toPlainText())
            cursor.execute("SELECT COUNT(*) FROM keyword WHERE clave = %s;",(clave))
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                dialogo = VentanaInformacion(self)
                dialogo.agregarTexto("Error\n\nNo existe un Keyword con esa clave")
                dialogo.show()
            else:
                cursor.execute("UPDATE keyword SET nombre = %s WHERE clave = %s;",(nombre,clave))
                dialogo = VentanaInformacion(self)
                dialogo.agregarTexto("Correcto\n\nKeyword modificada correctamente")
            dialogo.show()
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.txt_Clave.setText("")
            self.txt_Nombre.setText("")

class VentanaEliminar(QMainWindow):

    def __init__(self, parent=None):
        super(VentanaEliminar, self).__init__(parent)
        loadUi('V_Eliminar.ui', self)
        self.btn_Regresar.clicked.connect(self.abrirVentanaPrincipal)
        self.btn_Aceptar.clicked.connect(self.eliminarDatos)
        
    def eliminarDatos(self):
        try:
            cursor = conexion.cursor()
            clave = int(self.txt_Clave.toPlainText())
            cursor.execute("SELECT COUNT(*) FROM keyword WHERE clave = %s;",(clave))
            resultado = cursor.fetchone()
            if resultado[0] == 0:
                dialogo = VentanaInformacion(self)
                dialogo.agregarTexto("Error\n\nNo existe un Keyword con esa clave")
                dialogo.show()
            else:
                cursor.execute("DELETE FROM keyword WHERE clave = %s;",(clave))
                dialogo = VentanaInformacion(self)
                dialogo.agregarTexto("Correcto\n\nKeyword eliminada correctamente")
                dialogo.show()
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.txt_Clave.setText("")

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

class VentanaInformacion(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaInformacion, self).__init__(parent)
        loadUi('V_Informacion.ui', self)
        self.btn_Ok.clicked.connect(self.cerrarVentana)

    def cerrarVentana(self):
        self.hide()

    def agregarTexto(self, mensaje):
        self.lbl_Mensaje.setText(mensaje)
        self.lbl_Mensaje.setFont(QtGui.QFont("MS Shell Dlg 2", 10, QtGui.QFont.Bold))
        self.lbl_Mensaje.setStyleSheet('color: white')

class VentanaPregunta(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaPregunta, self).__init__(parent)
        loadUi('V_Pregunta.ui', self)
        self.btn_Si.clicked.connect(self.generarPDF)
        self.btn_No.clicked.connect(self.cerrarVentana)

    def cerrarVentana(self):
        self.hide()

    def agregarTexto(self, mensaje):
        self.lbl_Mensaje.setText(mensaje)
        self.lbl_Mensaje.setFont(QtGui.QFont("MS Shell Dlg 2", 10, QtGui.QFont.Bold))
        self.lbl_Mensaje.setStyleSheet('color: white')

    def generarPDF(self):
        try:
            l = 10
            j = 410

            c = canvas.Canvas("reportePDF.pdf")

            c.setFont("Helvetica", 20)
            
            c.drawImage('ImagenPrincipal.jpg', 45, 595, 502, 212)
            c.drawString(l, 550, "Empresa: Keyword Company")
            c.drawString(l, 520, "Reporte generado el día: "+ time.strftime("%d/%m/%y"))
            c.drawString(l, 490, "Generado por: Diego Aaron Figueroa Campos")
            c.drawString(l, 440, "Clave               Nombre")

            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM keyword;")
            datos = cursor.fetchall()

            for row in datos:
                clave = row[0]
                nombre = row[1]
                c.drawString(l, j, "     {0}".format(clave,nombre) +"               "+ "     {1}".format(clave,nombre))
                j -= 25
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            c.save()
            dialogo = VentanaInformacion(self)
            dialogo.agregarTexto("Correcto\n\nReportePDF generado correctamente")
            self.hide()
            dialogo.show()

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

def convertidor(misDatos):
    def cvt(datos):
        try:
            return ast.literal_eval(datos)
        except Exception as e:
            return str(datos)
    return tuple(map(cvt, misDatos))

# Función principal
def main():
    conexion()
    app = QApplication(sys.argv)
    main = VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())

#Inicia programa principal
if __name__ == "__main__" :
    main()