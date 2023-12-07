from flask import render_template, session, redirect, request, flash
from app_flask.modelos.modelo_evento import Evento
from app_flask import app

@app.route('/crear/evento', methods=['GET'])
def formulario_evento():
    if 'id_usuario' not in session:
        return redirect('/')
    return render_template('crear_evento.html')

