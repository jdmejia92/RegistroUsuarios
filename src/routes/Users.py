from flask import Blueprint, jsonify, request
from flask_expects_json import expects_json
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# Entities
from src.models.entities.User import User

# Models
from src.models.UserModel import UserModel

main = Blueprint('user_blueprint', __name__)

SCHEMA = {
    "type": "object",

    "properties": {
        "email": {"type": "string", "pattern": "^\\S+@\\S+\\.\\S+$", "format": "email"},
        "password": {"type": "string", "minLength": 6, "maxLength": 10}
    },
    "required": ["email", "password"]
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
        check_user = UserModel.get_user_email(email)

        if check_user != None:
            return jsonify({'message': "User already exists"}), 400
        else:
            affected_rows = UserModel.add_user(user)

            if affected_rows == 1:
                return jsonify(user.id)
            else:
                return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
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
        password = generate_password_hash(request.json["password"])
        user = User(id, email, str(password))

        affected_rows = UserModel.update_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "No user updated"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
