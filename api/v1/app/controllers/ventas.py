from flask import Flask, Blueprint, request, jsonify
from app.models.ventas import modeloVentas

ventas = Blueprint('ventas', __name__)

#Obtener

@ventas.route('/ventas', methods = ['GET'])
def obtener_ventas():
    id = request.args.get('id')

    if id:
        venta = modeloVentas.obtener_venta_id(id)
        if venta:
            return jsonify(venta), 200
        return jsonify({"error": "Venta no encontrada"}), 404
    
    ventas = modeloVentas.obtener_todos_ventas()
    return jsonify(ventas), 200

#Ingresar

@ventas.route('/ventas', methods = ['POST'])
def ingresar_venta():
    datos_venta = request.get_json()
    if not datos_venta:
        return jsonify({"error": "Datos de venta no ingresados"}), 404
    
    nuevo_id = modeloVentas.ingresar_venta(datos_venta)
    if nuevo_id:
        return jsonify({"mensaje": "Venta creada exitosamente en la base de datos con la siguiente ID: ", "id": nuevo_id}), 200
    return jsonify({"error": "Error al crear la nueva venta"}), 404

#Actualizar

@ventas.route('/ventas', methods = ['PUT'])
def actualizar_venta():
    id = request.args.get('id')
    datos_nuevos = request.get_json()

    if not id or not datos_nuevos:
        return jsonify({"error": "Se requieren la ID y los datos nuevos"}), 404
    
    actualizacion = modeloVentas.actualizar_venta(id, datos_nuevos)
    if actualizacion:
        return jsonify({"mensaje": "Información de la venta actualizada"}), 200
    return jsonify({"error": "Error en la actualización de la información"}), 404

#Eliminar

@ventas.route('/ventas', methods = ['DELETE'])
def eliminar_venta():
    id = request.args.get('id')

    if not id:
        return jsonify({"error": "Se requiere la ID"}), 404
    
    eliminado = modeloVentas.eliminar_venta(id)
    if eliminado:
        return jsonify({"mensaje": "Venta eliminada con éxito"}), 200
    return jsonify({"error": "Eliminación errónea de la venta"}), 404