from flask import Flask, Blueprint, request, jsonify
from app.models.marcas import modeloMarcas

marcas = Blueprint('marcas', __name__)

#Obtener

@marcas.route('/marcas', methods = ['GET'])
def obtener_marcas():
    id = request.args.get('id')

    if id:
        marca = modeloMarcas.obtener_marca_id(id)
        if marca:
            return jsonify(marca), 200
        return jsonify({"error": "Marca no encontrada"}), 404
    
    marcas = modeloMarcas.obtener_todos_marcas()
    return jsonify(marcas), 200

#Ingresar

@marcas.route('/marcas', methods = ['POST'])
def ingresar_marca():
    datos_marca = request.get_json()
    if not datos_marca:
        return jsonify({"error": "Datos de marca no ingresados"}), 404
    
    nuevo_id = modeloMarcas.ingresar_marca(datos_marca)
    if nuevo_id:
        return jsonify({"mensaje": "Marca creada exitosamente en la base de datos con la siguiente ID: ", "id": nuevo_id}), 200
    return jsonify({"error": "Error al crear la nueva marca"}), 404

#Actualizar

@marcas.route('/marcas', methods = ['PUT'])
def actualizar_marca():
    id = request.args.get('id')
    datos_nuevos = request.get_json()

    if not id or not datos_nuevos:
        return jsonify({"error": "Se requieren la ID y los datos nuevos"}), 404
    
    actualizacion = modeloMarcas.actualizar_marca(id, datos_nuevos)
    if actualizacion:
        return jsonify({"mensaje": "Información de la marca actualizada"}), 200
    return jsonify({"error": "Error en la actualización de la información"}), 404

#Eliminar

@marcas.route('/marcas', methods = ['DELETE'])
def eliminar_marca():
    id = request.args.get('id')

    if not id:
        return jsonify({"error": "Se requiere la ID"}), 404
    
    eliminado = modeloMarcas.eliminar_marca(id)
    if eliminado:
        return jsonify({"mensaje": "Marca eliminada con éxito"}), 200
    return jsonify({"error": "Eliminación errónea de la marca"}), 404