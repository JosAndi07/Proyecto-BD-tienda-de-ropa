from flask import Flask, Blueprint, request, jsonify
from app.models.usuarios import modeloUsuarios

usuarios = Blueprint('usuarios', __name__)

#Métodos para ejecutar los métodos de models; obtener todos, obtener por id, ingresar, actualizar y eliminar

#Obtener

@usuarios.route('/usuarios', methods = ['GET'])
def obtener_usuario():
    id = request.args.get('id')

    if id:
        usuario = modeloUsuarios.obtener_usuario_id(id)
        if usuario:
            return jsonify(usuario), 200
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    usuarios = modeloUsuarios.obtener_todos_usuarios()
    return jsonify(usuarios), 200

#Ingresar

@usuarios.route('/usuarios', methods = ['POST'])
def ingresar_usuario():
    datos_usuario = request.get_json()
    if not datos_usuario:
        return jsonify({"error": "Datos de usuario no ingresados"}), 404
    
    nuevo_id = modeloUsuarios.ingresar_usuario(datos_usuario)
    if nuevo_id:
        return jsonify({"mensaje": "Usuario creado exitosamente en la base de datos con la siguiente ID: ", "id": nuevo_id}), 200
    return jsonify({"error": "Error al crear el nuevo usuario"}), 404

#Actualizar

@usuarios.route('/usuarios', methods = ['PUT'])
def actualizar_usuario():
    id = request.args.get('id')
    datos_nuevos = request.get_json()

    if not id or not datos_nuevos:
        return jsonify({"error": "Se requieren la ID y los datos nuevos"}), 404
    
    actualizacion = modeloUsuarios.actualizar_usuario(id, datos_nuevos)
    if actualizacion:
        return jsonify({"mensaje": "Información del usuario actualizada"}), 200
    return jsonify({"error": "Error en la actualización de la información"}), 404

#Eliminar

@usuarios.route('/usuarios', methods = ['DELETE'])
def eliminar_usuario():
    id = request.args.get('id')

    if not id:
        return jsonify({"error": "Se requiere la ID"}), 404
    
    eliminado = modeloUsuarios.eliminar_usuario(id)
    if eliminado:
        return jsonify({"mensaje": "Usuario eliminado con éxito"}), 200
    return jsonify({"error": "Eliminación errónea del usuario"}), 404