from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS, EMAIL_REGEX

class Post:
    def __init__(self, datos):
        self.nombre_post = datos ['nombre_post']
        self.descripcion_post = datos ['descripcion_post']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.usuario_id = datos['usuario_id']
    
    @classmethod
    def crear_post(cls, datos):
        query = """
                INSERT INTO post(nombre_post, descripcion_post, usuario_id)
                VALUES(%(nombre_post)s, %(descripcion_post)s, %(usuario_id)s)
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)