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
        **request.form,
        'usuario_id': session['id_usuario']
    }
    Post.crear_post(nuevo_post)
    return redirect('/inicio')

    