from flask import render_template, session, redirect, request, flash
from app_flask.modelos.modelo_usuario import Usuario
from app_flask import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/', methods= ['GET'])
def login():
    return render_template('test_creacion.html')

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route('/procesa/registro', methods= ['POST'])
def process_register():
    if Usuario.validar_registro(request.form) == False:
        return render_template('test_login.html')
    encrypted_password = bcrypt.generate_password_hash(request.form['contraseña'])
    nuevo_usuario = {
        **request.form,
        'contraseña' : encrypted_password
    }
    id_usuario = Usuario.crear_uno(nuevo_usuario)
    session['id_usuario'] = id_usuario
    return redirect("/inicio")