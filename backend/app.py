from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde frontend

# Configuración de JWT
app.config["JWT_SECRET_KEY"] = "clave-super-secreta"
jwt = JWTManager(app)

# Simulación de base de datos
users = []

# Ruta raíz opcional
@app.route("/", methods=["GET"])
def home():
    return jsonify({"msg": "API de Refrigeración Industrial funcionando"}), 200

# 📌 Registro
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email") 
    password = data.get("password")

    if not email or not password:
        return jsonify({"msg": "Faltan datos"}), 400

    if any(user["email"] == email for user in users):
        return jsonify({"msg": "Usuario ya registrado"}), 409

    users.append({"email": email, "password": password})
    return jsonify({"msg": "Usuario registrado"}), 201

# 📌 Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = next((u for u in users if u["email"] == email and u["password"] == password), None)
    print(user)
    
    if not user:
        return jsonify({"msg": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=email)
    return jsonify({"token": access_token}), 200

# 🔐 Zona privada (protegida con token)
@app.route("/private", methods=["GET"])
@jwt_required()
def private():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Hola {current_user}, estás autenticado"}), 200

# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)
