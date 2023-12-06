from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask.modelos import modelo_usuario
from app_flask import BASE_DATOS, EMAIL_REGEX

class Post:
    def __init__(self, datos):
        self.nombre_post = datos ['nombre_post']
        self.descripcion_post = datos ['descripcion_post']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']
        self.usuario_id = datos['usuario_id']
        self.usuario = None
        self.num_comentarios = None
    
    @classmethod
    def crear_post(cls, datos):
        query = """
                INSERT INTO post(nombre_post, descripcion_post, usuario_id)
                VALUES(%(nombre_post)s, %(descripcion_post)s, %(usuario_id)s)
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)
    
    @classmethod
    def obtener_post_dashboard(cls):               ##función para mostrar información reducida en posts
        query = """
                SELECT post.*, COUNT(comentarios.idcomentarios) AS num_comentarios, usuarios.* FROM post 
                LEFT JOIN comentarios 
                ON comentarios.post_id = post.id
                JOIN usuarios
                ON usuarios.id = post.usuario_id
                GROUP BY post.id
                ORDER BY post.id DESC
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_posts = []
        for renglon in resultado:
            post = cls(renglon)
            usuario = {
                **renglon,
                'nombre' : renglon['nombre'],
                'id' : renglon['id'],
            }
            post.usuario = modelo_usuario.Usuario(usuario)
            post.num_comentarios = renglon['num_comentarios']
            lista_posts.append(post)
        return lista_posts
    
    @classmethod
    def obtener_posts_perfil(cls, datos):               ##función para mostrar información reducida en posts
        query = """
                SELECT post.*, COUNT(comentarios.idcomentarios) AS num_comentarios, usuarios.* FROM post 
                LEFT JOIN comentarios 
                ON comentarios.post_id = post.id
                JOIN usuarios
                ON usuarios.id = post.usuario_id
                WHERE nombre_usuario = %(nombre_usuario)s
                GROUP BY post.id
                ORDER BY post.id DESC
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        lista_posts = []
        for renglon in resultado:
            post = cls(renglon)
            usuario = {
                **renglon,
                'nombre' : renglon['nombre'],
                'id' : renglon['id'],
            }
            post.usuario = modelo_usuario.Usuario(usuario)
            post.num_comentarios = renglon['num_comentarios']
            lista_posts.append(post)
        return lista_posts
        