from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://andresjmb20:perseusgrc99@cluster0.opbpzao.mongodb.net/proyecto-BD-tienda-ropa"
    mongo.init_app(app)
    CORS(app)

    from .controllers.libros import libros

    app.register_blueprint(libros, url_prefix="/proyecto-BD-tienda-ropa/api/v1")

    CORS(app, origins="*")

    return app