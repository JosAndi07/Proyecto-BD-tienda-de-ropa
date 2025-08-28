#Importación de las librerías flask

import os
from flask import Flask, send_from_directory
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()

#Inicio y conexión con Mongo
def create_app():
    app = Flask(__name__, static_folder="front-end")
    app.config["MONGO_URI"] = "mongodb+srv://andresjmb20:perseusgrc99@cluster0.opbpzao.mongodb.net/tienda-ropaBD"
    mongo.init_app(app)
    CORS(app, origins="*")

    @app.route('/')
    def inicio():
        return send_from_directory(app.static_folder, "principal.html")
    
    @app.route('/<path:nombre_archivo>')
    def cargar_html(nombre_archivo):
        return send_from_directory(app.static_folder, nombre_archivo)

    #Conexión de los endpoints
    from .controllers.usuarios import usuarios
    app.register_blueprint(usuarios, url_prefix="/proyecto-BD-tienda-ropa/api/v1")

    from .controllers.marcas import marcas
    app.register_blueprint(marcas, url_prefix="/proyecto-BD-tienda-ropa/api/v1")

    from .controllers.prendas import prendas
    app.register_blueprint(prendas, url_prefix="/proyecto-BD-tienda-ropa/api/v1")

    from .controllers.ventas import ventas
    app.register_blueprint(ventas, url_prefix="/proyecto-BD-tienda-ropa/api/v1")

    CORS(app, origins="*")

    return app