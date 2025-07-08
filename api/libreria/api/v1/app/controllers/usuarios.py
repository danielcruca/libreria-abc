from flask import Blueprint, request, jsonify
from app.models.usuario import UsuarioModel

usuarios_endpoint = Blueprint('usuarios_endpoint', __name__)
# GET todos los usuarios sin parametros y con id.
# Ejemplo de endpoint:
# http://127.0.0.1:5000/libreria/api/v1/usuarios?id=6823e02cea9cb5e5156c4bd9
# http://127.0.0.1:5000/libreria/api/v1/usuarios

@usuarios_endpoint.route('/usuarios', methods=['GET'])
def obtenerUsuarios():
    id_usuario = request.args.get('id')

    #Id de usuario es opcional.
    if id_usuario:
        # Si el id esta incluido en la url, se obtiene el usuario por id
        usuario = UsuarioModel.obtener_por_id(id_usuario)
        if usuario:
            return jsonify(usuario), 200
        return jsonify({"error": "Usuario no encontrado"}), 404
    # Aca se obitne todos los usuarios
    usuarios = UsuarioModel.obtener_todos()
    return jsonify(usuarios), 200

 