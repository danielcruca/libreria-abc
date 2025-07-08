from bson.objectid import ObjectId
from app import mongo

class LibroModel:
    @staticmethod
    def obtener_todos():
        print(mongo.db.list_collection_names())  # Asegúrate de que 'libros' exista
        libros_cursor = mongo.db.libros.find()
        libros = []
        for libro in libros_cursor:
            libro["_id"] = str(libro["_id"])
            libros.append(libro)
        return libros

    @staticmethod
    def obtener_por_id(id):
        try:
            libro = mongo.db.libros.find_one({"_id": ObjectId(id)})
            if libro:
                libro["_id"] = str(libro["_id"])
            return libro
        except:
            return None
