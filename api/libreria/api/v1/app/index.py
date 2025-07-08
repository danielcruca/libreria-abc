from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()

def create_app():
    # Se especifica la URI de mongo.
    app = Flask(__name__)
    #app.config["MONGO_URI"] = "mongodb://localhost:27017/libreria"
    app.config["MONGO_URI"] = "mongodb+srv://docentedanielcr:64BMvIy7ZF5Ylahy@cluster0.rnphuit.mongodb.net/libreria?retryWrites=true&w=majority"
    mongo.init_app(app)
    # Importante esto, esto es para que funcione el CORS y no tener problemas de seguridad.
    CORS(app)
    

    from .controllers.libros import libros_endpoints
    from .controllers.usuarios import usuarios_endpoint

    app.register_blueprint(libros_endpoints, url_prefix="/libreria/api/v1")
    app.register_blueprint(usuarios_endpoint, url_prefix="/libreria/api/v1")


    #CORS(app, origins=["http://localhost:3000"])
    CORS(app, origins="*")

    return app
