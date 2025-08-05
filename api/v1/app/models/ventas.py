from bson.objectid import ObjectId
from app import mongo

#Clase principal
class modeloVentas:

    #Método para obtener todas las ventas de la base de datos
    @staticmethod
    def obtener_todos_ventas():
        print(mongo.db.list_collection_names())
        ventas_cursor = mongo.db.ventas.find()
        ventas = []
        for venta in ventas_cursor:
            venta["_id"] = str(venta["_id"])
            ventas.append(venta)
        return ventas
    
    #Método para obtener una sola venta por su id respectiva
    @staticmethod
    def obtener_venta_id(id):
        try:
            venta = mongo.db.ventas.find_one({"_id": ObjectId(id)})
            if venta:
                venta["_id"] = str(venta["_id"])
            return venta
        except:
            return None
    
    #Método para ingresar una nueva venta en la base de datos
    @staticmethod
    def ingresar_venta(datos_venta):
        try:
            venta = mongo.db.ventas.insert_one(datos_venta)
            return str(venta.inserted_id)
        except Exception as e:
            print(f"Error al ingresar nuevo venta: {e}")
            return None
    
    #Método para actualizar los datos de una venta
    @staticmethod
    def actualizar_venta(id, datos_nuevos):
        try:
            venta = mongo.db.ventas.update_one(
                {"_id": ObjectId(id)},
                {"$set": datos_nuevos}
            )
            return venta.modified_count > 0
        except Exception as e:
            print(f"Error al actualizar los datos del venta: {e}")
            return False
    
    #Método para eliminar una venta en la base de datos
    @staticmethod
    def eliminar_venta(id):
        try:
            venta = mongo.db.ventas.delete_one({"_id": ObjectId(id)})
            return venta.deleted_count > 0
        except Exception as e:
            print(f"Error al eliminar venta: {e}")
            return False