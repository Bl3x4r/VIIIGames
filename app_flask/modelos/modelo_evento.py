from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask.modelos import modelo_usuario
from app_flask import BASE_DATOS, EMAIL_REGEX

class Evento:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre_evento = datos['nombre_evento']
        self.descripcion_evento = datos['descripcion_evento']
        self.lugar = datos['lugar']
        self.fecha_evento = datos['fecha_evento']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.usuario_id = datos['usuario_id']
        self.comunidad = datos['comunidad']
        self.usuario = None

    @classmethod
    def obtener_evento_dashboard(cls):              
        query = """
                SELECT eventos.*, usuarios.* FROM eventos 
                JOIN usuarios
                ON usuarios.id = eventos.usuario_id
                GROUP BY eventos.id
                ORDER BY eventos.id DESC
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_eventos = []
        for renglon in resultado:
            evento = cls(renglon)
            usuario = {
                **renglon,
                'nombre' : renglon['nombre'],
                'id' : renglon['id'],
            }
            evento.usuario = modelo_usuario.Usuario(usuario)
            lista_eventos.append(evento)
        return lista_eventos