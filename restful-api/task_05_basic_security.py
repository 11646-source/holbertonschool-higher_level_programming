#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"
jwt = JWTManager(app)

# In-memory user store
users = {
    "admin": {
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    },
    "john": {
        "password": generate_password_hash("johnpass"),
        "role": "user"
    }
}

# -------------------------
# Basic Authentication
# -------------------------
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify({"message": f"Hello, {auth.current_user()}! You accessed with Basic Auth."})


# -------------------------
# JWT Authentication
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed role in JWT payload
    access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    identity = get_jwt_identity()
    return jsonify({"message": f"Hello, {identity['username']}! You accessed with JWT."})


# -------------------------
# Role-based Access Control
# -------------------------
def role_required(required_role):
    def wrapper(fn):
        def decorator(*args, **kwargs):
            claims = get_jwt_identity()
            if claims["role"] != required_role:
                return jsonify({"error": "Access forbidden: insufficient role"}), 403
            return fn(*args, **kwargs)
        decorator.__name__ = fn.__name__
        return decorator
    return wrapper

@app.route("/admin-only")
@jwt_required()
@role_required("admin")
def admin_only():
    identity = get_jwt_identity()
    return jsonify({"message": f"Welcome Admin {identity['username']}!"})


if __name__ == "__main__":
    app.run()
