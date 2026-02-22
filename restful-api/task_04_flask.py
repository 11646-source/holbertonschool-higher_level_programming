#!/usr/bin/python3
"""Simple Flask API example."""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        user_data = users[username].copy()
        user_data["username"] = username
        return jsonify(user_data)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    user_data = users[username].copy()
    user_data["username"] = username
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run()

