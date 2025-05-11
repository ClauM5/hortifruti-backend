from flask import Flask, jsonify
from flask_cors import CORS  # Importando CORS para configurar as permissões

app = Flask(__name__)

# Habilitando o CORS para todas as origens
CORS(app)

# Simulação de uma API de produtos
@app.route("/api/produtos", methods=["GET"])
def get_produtos():
    produtos = [
        {"id": 1, "nome": "Maçã", "preco": 3.5},
        {"id": 2, "nome": "Banana", "preco": 2.0},
        {"id": 3, "nome": "Laranja", "preco": 4.0},
        {"id": 4, "nome": "Tomate", "preco": 5.5},
    ]
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)
