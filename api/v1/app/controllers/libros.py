from flask import Flask, Blueprint, request, jsonify
from app.models.libros import modeloLibros

libros = Blueprint('libros', __name__)

@libros.route('/libros', methods = ['GET'])

#def obtener_libros():
#    id_libro = request.args.get('id')
#    if id_libro is not None:
#        return f"ID del libro: {id_libro}", 200
#    else:
#        return "Vacío", 200

def obtener_libros():
    id = request.args.get('id')

    if id:
        libro = modeloLibros.obtener_libro_id(id)
        if libro:
            return jsonify(libro), 200
        return jsonify({"error": "Libro no encontrado"}), 404
    
    libros = modeloLibros.obtener_todos_libros()
    return jsonify(libros), 200