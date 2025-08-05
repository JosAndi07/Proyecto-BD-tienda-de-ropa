from bson.objectid import ObjectId
from app import mongo

#Clase principal
class modeloPrendas:

    #Método para obtener todas las prendas de la base de datos
    @staticmethod
    def obtener_todos_prendas():
        print(mongo.db.list_collection_names())
        prendas_cursor = mongo.db.prendas.find()
        prendas = []
        for prenda in prendas_cursor:
            prenda["_id"] = str(prenda["_id"])
            prendas.append(prenda)
        return prendas
    
    #Método para obtener una sola prenda por su id respectiva
    @staticmethod
    def obtener_prenda_id(id):
        try:
            prenda = mongo.db.prendas.find_one({"_id": ObjectId(id)})
            if prenda:
                prenda["_id"] = str(prenda["_id"])
            return prenda
        except:
            return None
    
    #Método para ingresar una nueva prenda en la base de datos
    @staticmethod
    def ingresar_prenda(datos_prenda):
        try:
            prenda = mongo.db.prendas.insert_one(datos_prenda)
            return str(prenda.inserted_id)
        except Exception as e:
            print(f"Error al ingresar nuevo prenda: {e}")
            return None
    
    #Método para actualizar los datos de una prenda
    @staticmethod
    def actualizar_prenda(id, datos_nuevos):
        try:
            prenda = mongo.db.prendas.update_one(
                {"_id": ObjectId(id)},
                {"$set": datos_nuevos}
            )
            return prenda.modified_count > 0
        except Exception as e:
            print(f"Error al actualizar los datos del prenda: {e}")
            return False
    
    #Método para eliminar una prenda en la base de datos
    @staticmethod
    def eliminar_prenda(id):
        try:
            prenda = mongo.db.prendas.delete_one({"_id": ObjectId(id)})
            return prenda.deleted_count > 0
        except Exception as e:
            print(f"Error al eliminar prenda: {e}")
            return False