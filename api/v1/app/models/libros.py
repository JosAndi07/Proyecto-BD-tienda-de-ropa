from bson.objectid import ObjectId
from app import mongo

#Clase principal
class modeloLibros:

    #Método para obtener todos los libros de la base de datos
    @staticmethod
    def obtener_todos_libros():
        print(mongo.db.list_collection_names())
        libros_cursor = mongo.db.libros.find()
        libros = []
        for libro in libros_cursor:
            libro["_id"] = str(libro["_id"])
            libros.append(libro)
        return libros
    
    #Método para obtener un solo libro por su id respectiva
    @staticmethod
    def obtener_libro_id(id):
        try:
            libro = mongo.db.libros.find_one({"_id": ObjectId(id)})
            if libro:
                libro["_id"] = str(libro["_id"])
            return libro
        except:
            return None
    
    #Método para ingresar un nuevo libro en la base de datos
    @staticmethod
    def ingresar_libro(datos_libro):
        try:
            libro = mongo.db.libros.insert_one(datos_libro)
            return str(libro.inserted_id)
        except Exception as e:
            print(f"Error al ingresar nuevo libro: {e}")
            return None
    
    #Método para actualizar los datos de un libro
    @staticmethod
    def actualizar_libro(id, nuevos_datos):
        try:
            libro = mongo.db.libros.update_one(
                {"_id": ObjectId(id)},
                {"$set": nuevos_datos}
            )
            return libro.modified_count > 0
        except Exception as e:
            print(f"Error al actualizar los datos del libro: {e}")
            return False
    
    #Método para eliminar un libro en la base de datos
    @staticmethod
    def eliminar_libro(id):
        try:
            libro = mongo.db.libros.delete_one({"_id": ObjectId(id)})
            return libro.deleted_count > 0
        except Exception as e:
            print(f"Error al eliminar libro: {e}")
            return False