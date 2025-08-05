from flask import Flask, Blueprint, request, jsonify
from app.models.prendas import modeloPrendas

prendas = Blueprint('prendas', __name__)

#Obtener

@prendas.route('/prendas', methods = ['GET'])
def obtener_prendas():
    id = request.args.get('id')

    if id:
        prenda = modeloPrendas.obtener_prenda_id(id)
        if prenda:
            return jsonify(prenda), 200
        return jsonify({"error": "Prenda no encontrada"}), 404
    
    prendas = modeloPrendas.obtener_todos_prendas()
    return jsonify(prendas), 200

#Ingresar

@prendas.route('/prendas', methods = ['POST'])
def ingresar_prenda():
    datos_prenda = request.get_json()
    if not datos_prenda:
        return jsonify({"error": "Datos de prenda no ingresados"}), 404
    
    nuevo_id = modeloPrendas.ingresar_prenda(datos_prenda)
    if nuevo_id:
        return jsonify({"mensaje": "Prenda creada exitosamente en la base de datos con la siguiente ID: ", "id": nuevo_id}), 200
    return jsonify({"error": "Error al crear la nueva prenda"}), 404

#Actualizar

@prendas.route('/prendas', methods = ['PUT'])
def actualizar_prenda():
    id = request.args.get('id')
    datos_nuevos = request.get_json()

    if not id or not datos_nuevos:
        return jsonify({"error": "Se requieren la ID y los datos nuevos"}), 404
    
    actualizacion = modeloPrendas.actualizar_prenda(id, datos_nuevos)
    if actualizacion:
        return jsonify({"mensaje": "Información de la prenda actualizada"}), 200
    return jsonify({"error": "Error en la actualización de la información"}), 404

#Eliminar

@prendas.route('/prendas', methods = ['DELETE'])
def eliminar_prenda():
    id = request.args.get('id')

    if not id:
        return jsonify({"error": "Se requiere la ID"}), 404
    
    eliminado = modeloPrendas.eliminar_prenda(id)
    if eliminado:
        return jsonify({"mensaje": "Prenda eliminada con éxito"}), 200
    return jsonify({"error": "Eliminación errónea de la prenda"}), 404