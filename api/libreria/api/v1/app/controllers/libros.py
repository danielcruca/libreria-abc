from flask import Blueprint, request, jsonify
from app.models.libro import LibroModel

libros_endpoints = Blueprint('libros_endpoints', __name__)
 
# GET todos los libros sin parametros y con id.
# Ejemplo de endpoint:
# http://127.0.0.1:5000/libreria/api/v1/libros?id=6823e02cea9cb5e5156c4bd3
# http://127.0.0.1:5000/libreria/api/v1/libros

@libros_endpoints.route('/libros', methods=['GET'])
def obtenerLibros():
    idLibro = request.args.get('id')

    if idLibro:
        libro = LibroModel.obtener_por_id(idLibro)
        if libro:
            return jsonify(libro), 200
        return jsonify({"error": "Libro no encontrado"}), 404

    libros = LibroModel.obtener_todos()
    return jsonify(libros), 200

