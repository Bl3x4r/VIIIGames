from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS, EMAIL_REGEX

class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre_usuario = datos['nombre_usuario']
        self.nombre =  datos['nombre']
        self.apellido = datos['apellido']
        self.correo =  datos['correo']
        self.contraseña = datos['contraseña']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']