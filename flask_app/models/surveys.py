from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.idioma = data['idioma']
        self.comentario = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    #guardar info encuesta
    @classmethod
    def save(cls, data):
        print("Entrar a save", data)
        query = "INSERT INTO surveys (nombre, ubicacion, idioma, comentario) VALUES (%(nombre)s, %(ubicacion)s, %(idioma)s, %(comentario)s)"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query, data)
        return result



    
    @classmethod
    def get_survey(cls):
        query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        print("Resultado", result)
        return Survey(result[0])
    



    #validar info
    @staticmethod
    def is_valid(survey):
        is_valid = True

        if len(survey['nombre']) < 3:
            is_valid = False
            print("fallo nombre")
            flash("El nombre debe tener 3 caracteres")

        if len(survey['ubicacion']) < 1:
            is_valid = False
            print("fallo ubicacion")
            flash("Elegir ubicacion")

        if len(survey['idioma']) < 1:
            is_valid = False
            print("Fallo idioma")
            flash("Elegir idioma")
    
        if len(survey['comentario']) < 3:
            is_valid = False
            print("Fallo comentario")
            flash("El comentario debe tener 3 caracteres")

        return is_valid