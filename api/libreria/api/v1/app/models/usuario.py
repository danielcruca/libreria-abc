from bson.objectid import ObjectId
from app import mongo

class UsuarioModel:
    @staticmethod
    def obtener_todos():
        usuarios_cursor = mongo.db.usuarios.find() 
        # Equivalente a: select * from usuarios
        usuarios = []
        for usuario in usuarios_cursor:
            usuario["_id"] = str(usuario["_id"])
            usuarios.append(usuario)
        return usuarios


    @staticmethod
    def obtenerPorId(id):
        try:
            usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id)})
            # Equivalente a: select * from usuarios where id = id
            if usuario:
                usuario["_id"] = str(usuario["_id"])
            return usuario
        except:
            return None
        
        
    @staticmethod
    def obtener_por_id(id):
        print(" este es el id", id )
        try:
            usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id)})
            # Equivalente a: select * from usuarios where id = id
            if usuario:
                usuario["_id"] = str(usuario["_id"])
            return usuario
        except:
            return None

    @staticmethod
    def eliminar(id):
        try:
            result = mongo.db.usuarios.delete_one({"_id": ObjectId(id)})
            return result.deleted_count
        except:
            return -1
