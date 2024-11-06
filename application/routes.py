from flask import Blueprint, jsonify, request
from app.models import User
from bson import ObjectId

main = Blueprint("main", __name__)

@main.route("/users", methods=["GET"])
def get_users():
    users = User.get_users()
    return jsonify([{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]), 200

@main.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = User.get_user_by_id(ObjectId(id))
    if user:
        return jsonify({"id": str(user["_id"]), "name": user["name"], "email": user["email"]}), 200
    return jsonify({"error": "User not found"}), 404

@main.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if "name" in data and "email" in data and "password" in data:
        user_id = User.create_user(data)
        return jsonify({"id": str(user_id.inserted_id), "message": "User created"}), 201
    return jsonify({"error": "Invalid data"}), 400

@main.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    result = User.update_user(ObjectId(id), data)
    if result.modified_count > 0:
        return jsonify({"message": "User updated"}), 200
    return jsonify({"error": "User not found or data unchanged"}), 404

@main.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = User.delete_user(ObjectId(id))
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404
