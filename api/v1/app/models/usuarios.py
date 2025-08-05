from bson.objectid import ObjectId
from app import mongo

#Clase principal
class modeloUsuarios:

    #Método para obtener todos los usuarios de la base de datos
    @staticmethod
    def obtener_todos_usuarios():
        print(mongo.db.list_collection_names())
        usuarios_cursor = mongo.db.usuarios.find()
        usuarios = []
        for usuario in usuarios_cursor:
            usuario["_id"] = str(usuario["_id"])
            usuarios.append(usuario)
        return usuarios
    
    #Método para obtener un solo usuario por su id respectiva
    @staticmethod
    def obtener_usuario_id(id):
        try:
            usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id)})
            if usuario:
                usuario["_id"] = str(usuario["_id"])
            return usuario
        except:
            return None
    
    #Método para ingresar un nuevo usuario en la base de datos
    @staticmethod
    def ingresar_usuario(datos_usuario):
        try:
            usuario = mongo.db.usuarios.insert_one(datos_usuario)
            return str(usuario.inserted_id)
        except Exception as e:
            print(f"Error al ingresar nuevo usuario: {e}")
            return None
    
    #Método para actualizar los datos de un usuario
    @staticmethod
    def actualizar_usuario(id, datos_nuevos):
        try:
            usuario = mongo.db.usuarios.update_one(
                {"_id": ObjectId(id)},
                {"$set": datos_nuevos}
            )
            return usuario.modified_count > 0
        except Exception as e:
            print(f"Error al actualizar los datos del usuario: {e}")
            return False
    
    #Método para eliminar un usuario en la base de datos
    @staticmethod
    def eliminar_usuario(id):
        try:
            usuario = mongo.db.usuarios.delete_one({"_id": ObjectId(id)})
            return usuario.deleted_count > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False