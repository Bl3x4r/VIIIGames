from flask import render_template, session, redirect, request, flash
from app_flask.modelos.modelo_usuario import Usuario
from app_flask.modelos.modelo_post import Post
from app_flask import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/', methods= ['GET'])
def login():
    return redirect('/inicio')

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route('/registrarse')
def formulario_registro():
    return render_template('test_creacion.html')

@app.route('/iniciar/sesion')
def iniciar_sesion():
    return render_template("test_Login.html")

@app.route('/procesa/registro', methods= ['POST'])
def process_register():
    if Usuario.validar_registro(request.form) == False:
        return render_template('test_creacion.html')
    encrypted_password = bcrypt.generate_password_hash(request.form['contraseña'])
    nuevo_usuario = {
        **request.form,
        'contraseña' : encrypted_password
    }
    id_usuario = Usuario.crear_uno(nuevo_usuario)
    
    session['id_usuario'] = id_usuario
    return redirect("/inicio")

@app.route('/procesa/login', methods=["POST"])
def procesa_login():
    usuario_login = Usuario.obtener_uno(request.form)
    if usuario_login == None:
        flash('Este usuario no exite', 'error_login')
        return redirect("/iniciar/sesion")
    if not bcrypt.check_password_hash(usuario_login.contraseña, request.form['contraseña']):
        flash('Credenciales Incorrectas', 'error_login')
        return redirect("/iniciar/sesion")
    session['id_usuario'] = usuario_login.id
    session['nombre_usuario'] = usuario_login.nombre_usuario
    return redirect("/inicio")

@app.route('/perfil/<string:pf_nombre_usuario>', methods=['GET'])
def desplegar_perfil(pf_nombre_usuario):
    usr_dict = { "nombre_usuario" : pf_nombre_usuario}
    usuario_perfil = Usuario.obtener_uno(usr_dict)
    posts_perfil = Post.obtener_posts_perfil(usr_dict)
    return render_template("perfil.html", usuario_perfil = usuario_perfil, posts_perfil = posts_perfil)

@app.route("/cerrar/sesion" , methods=["GET"])
def procesa_logout():
    session.clear()
    return redirect("/")