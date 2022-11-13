from flask import Blueprint, jsonify, request
from flask_expects_json import expects_json
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

# Entities
from src.models.entities.User import User

# Models
from src.models.UserModel import UserModel

main = Blueprint('user_blueprint', __name__)

# Cambiar el tipo de dominio de correo que desees autentificar en pattern
SCHEMA = {
    "type": "object",

    "properties": {
        "email": {"type": "string", "pattern": "^\\S+@system.\\S+$", "format": "email"},
        "password": {"type": "string", "minLength": 6, "maxLength": 10}
    },
    "required": ["email", "password"]
}

SCHEMA_PASSWORD = {
    "type": "object",

    "properties": {
        "password": {"type": "string", "minLength": 6, "maxLength": 10}
    },
    "required": ["password"]
}


@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
@expects_json(SCHEMA)
def add_user():
    try:
        email = request.json["email"]
        password = generate_password_hash(request.json["password"])
        id = uuid.uuid4()
        user = User(str(id), email, str(password))

        affected_rows = UserModel.add_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        if type(ex) == psycopg2.errors.UniqueViolation:
            return jsonify({'message': 'The user already exist'}), 400
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User(id)

        affected_rows = UserModel.delete_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "No user deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
@expects_json(SCHEMA)
def update_user(id):
    try:
        email = request.json["email"]
        password = request.json["password"]

        user = User(id, email, str(password))

        affected_rows = UserModel.update_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "No user updated"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/password/<email>', methods=['PUT'])
@expects_json(SCHEMA_PASSWORD)
def update_password(email):
    try:
        password = request.json["password"]

        user_check = UserModel.get_user_email(email)

        check_new_password = check_password_hash(user_check['password'], password)

        if check_new_password == True:
            return jsonify({'message': 'Most use a new password'}), 400
        else:
            hashPassword = generate_password_hash(password)
            user = User(user_check['id'], email, str(hashPassword))

            affected_rows = UserModel.update_password(user)

            if affected_rows == 1:
                return jsonify(user.id)
            else:
                return jsonify({'message': "No password updated"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
