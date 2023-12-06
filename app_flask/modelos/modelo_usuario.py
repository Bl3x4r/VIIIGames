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
        self.tipo_usuario = 0
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def obtener_uno(cls, datos):
        query = """
                SELECT * FROM usuarios
                WHERE nombre_usuario = %(nombre_usuario)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) == 0:
            return None
        return Usuario(resultado[0])

    @classmethod
    def crear_uno(cls, datos):
        query = """
                INSERT INTO usuarios(nombre_usuario, nombre, apellido, correo, contraseña)
                VALUES (%(nombre_usuario)s,%(nombre)s,%(apellido)s,%(correo)s,%(contraseña)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)

    @staticmethod
    def validar_registro(datos):
        valid = True
        if len(datos['nombre_usuario']) < 2:
            valid = False
            flash('Por favor escribe tu nombre de usuario.' , 'error_nombre_usuario')
        if len(datos['nombre']) < 2:
            valid = False
            flash('Por favor escribe tu nombre.', 'error_nombre')
        if len(datos['apellido']) < 2:
            valid = False
            flash('Por favor escribe tu apellido.', 'error_apellido')
        if not EMAIL_REGEX.match(datos['correo']):
            valid = False
            flash('Please enter a valid email.')
        if datos['contraseña'] != datos['confirmar_contraseña']:
            valid = False
            flash('Las contraseñas mo coinciden.', 'error_contraseña')
        if len(datos['contraseña']) <8:
            valid = False
            flash('La contraseña debe tener al menos 8 caracteres.', 'error_contraseña')
        return valid