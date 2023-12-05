from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS, EMAIL_REGEX

class Post:
    def __init__(self, datos):
        self.nombre_post = datos ['nombre_post']
        self.descripcion_post = datos ['descripcion_post']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']