from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"id": 1, "nombre": "Usuario1"},
    {"id": 2, "nombre": "Usuario2"}
]

@app.route('/')
def home():
    return "API funcionando"

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    data = request.json
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": data["nombre"]
    }
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario)

if __name__ == '__main__':
    app.run(debug=True)