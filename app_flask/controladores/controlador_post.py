from flask import render_template, session, redirect, request, flash
from app_flask.modelos.modelo_post import Post
from app_flask import app

@app.route('/crear/post', methods=['GET'])
def formulario_post():
    if 'id_usuario' not in session:
        return redirect('/')
    return render_template('crear_post.html')

@app.route('/procesar/creacion_post', methods=['POST'])
def crear_post():
    nuevo_post= {
        'nombre_post': request.form['nombre_post'],
        'descripcion_post': request.form['descripcion_post'],
        'usuario_id': session['id_usuario']
    }
    Post.crear_post(nuevo_post)
    return redirect('/inicio')

@app.route('/dashboard', methods=['GET'])
def renderizar_dashboard_posts():
    if 'id_usuario' not in session:
        return redirect('/')
    lista_posts = Post.obtener_post_dashboard()
    return render_template('tablero.html', lista_posts = lista_posts)