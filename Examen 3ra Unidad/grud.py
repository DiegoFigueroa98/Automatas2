from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from reportlab.pdfgen import canvas
import time

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('dashboard.html')

@app.route('/showDashBoard')
def showDashBoard():
    return render_template('dashboard.html')

@app.route('/showAgregar')
def showAgregar():
    return render_template('agregar.html')

@app.route('/showEliminar')
def showEliminar():
    return render_template('eliminar.html')

@app.route('/showModificar')
def showModificar():
    return render_template('modificar.html')

@app.route('/showReporte')
def showReporte():
    mysql = MySQL()
 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()

    cursor = conn.cursor()

    cadena = "select * from workers"

    cursor.execute(cadena)

    data = cursor.fetchall()

    conn.commit()

    return render_template('reporte.html', datos = data)

@app.route('/Agregar',methods=['POST'])
def Agregar():

    nombre = request.form['inputNombre']
    sueldo = request.form['inputSueldo']
    
    mysql = MySQL()
 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()

    cursor = conn.cursor()

    cadena = "INSERT INTO workers (nombre, sueldo) VALUES ('" + nombre + "','" + sueldo + "')"

    cursor.execute(cadena)

    data = cursor.fetchall()


    if len(data) is 0:
        
        conn.commit()
        return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})


@app.route('/Eliminar',methods=['POST'])
def Eliminar():

    clave = request.form['inputClave']
    
    mysql = MySQL()
 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()

    cursor = conn.cursor()

    cadena = "DELETE FROM workers WHERE clave = '" + clave + "'"

    cursor.execute(cadena)

    data = cursor.fetchall()

    

    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})


@app.route('/Modificar',methods=['POST'])
def Modificar():

    clave = request.form['inputClave']
    nombre = request.form['inputNombre']
    sueldo = request.form['inputSueldo']
    
    mysql = MySQL()
 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()

    cursor = conn.cursor()

    cadena = "UPDATE workers SET nombre = '" + nombre + "', sueldo = '" + sueldo + "' WHERE clave = '" + clave + "'"

    cursor.execute(cadena)
    
    conn.commit()
    return json.dumps({'message':'User created successfully !'})

@app.route('/Reporte',methods=['POST'])
def Reporte():

    ml = 10
    t = "                          "
    j = 740

    c = canvas.Canvas('Reporte.pdf')

    c.drawString(ml, 830, "Empresa: La Gran Empresa")
    c.drawString(ml, 810, "Reporte generado el: " + time.strftime("%d/%m/%y"))
    c.drawString(ml, 760, "Clave" + t + "Nombre" + t + "Sueldo")

    mysql = MySQL()
 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()

    cursor = conn.cursor()

    cadena = "select * from workers"

    cursor.execute(cadena)

    data = cursor.fetchall()


    for row in data:
        clave1 = row[0]
        nombre1 = row[1]
        sueldo1 = row[2]
        c.drawString(ml, j, "    {0}".format(clave1,nombre1,sueldo1) + t + "   {1}".format(clave1,nombre1,sueldo1) + t + "   {2}".format(clave1,nombre1,sueldo1))
        j = j - 15
    
    conn.commit()

    c.save()

    return json.dumps({'message':'User created successfully !'})

if __name__ == "__main__":
    app.run()