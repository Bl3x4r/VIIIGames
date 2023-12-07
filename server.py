from app_flask.controladores import controlador_usuario, controlador_post
from app_flask import app
from flask import render_template

@app.route('/conocer/equipo')
def desplegar_informacion_equipo():
    return render_template("conocenos.html")

@app.route('/mision')
def desplegar_mision_pagina():
    return render_template("Mision.html")

if __name__ == '__main__':
    app.run(debug = True)