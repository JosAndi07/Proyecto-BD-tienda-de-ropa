from bson.objectid import ObjectId
from app import mongo

#Clase principal
class modeloMarcas:

    #Método para obtener todas las marcas de la base de datos
    @staticmethod
    def obtener_todos_marcas():
        print(mongo.db.list_collection_names())
        marcas_cursor = mongo.db.marcas.find()
        marcas = []
        for marca in marcas_cursor:
            marca["_id"] = str(marca["_id"])
            marcas.append(marca)
        return marcas
    
    #Método para obtener una sola marca por su id respectiva
    @staticmethod
    def obtener_marca_id(id):
        try:
            marca = mongo.db.marcas.find_one({"_id": ObjectId(id)})
            if marca:
                marca["_id"] = str(marca["_id"])
            return marca
        except:
            return None
    
    #Método para ingresar una nueva marca en la base de datos
    @staticmethod
    def ingresar_marca(datos_marca):
        try:
            marca = mongo.db.marcas.insert_one(datos_marca)
            return str(marca.inserted_id)
        except Exception as e:
            print(f"Error al ingresar nuevo marca: {e}")
            return None
    
    #Método para actualizar los datos de una marca
    @staticmethod
    def actualizar_marca(id, datos_nuevos):
        try:
            marca = mongo.db.marcas.update_one(
                {"_id": ObjectId(id)},
                {"$set": datos_nuevos}
            )
            return marca.modified_count > 0
        except Exception as e:
            print(f"Error al actualizar los datos del marca: {e}")
            return False
    
    #Método para eliminar una marca en la base de datos
    @staticmethod
    def eliminar_marca(id):
        try:
            marca = mongo.db.marcas.delete_one({"_id": ObjectId(id)})
            return marca.deleted_count > 0
        except Exception as e:
            print(f"Error al eliminar marca: {e}")
            return False