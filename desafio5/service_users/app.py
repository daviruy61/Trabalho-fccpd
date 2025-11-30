from flask import Flask, jsonify

app = Flask(__name__)

USER_REGISTRY = [
    {"id": 10, "nome": "Pedro Alves",   "cidade": "Curitiba"},
    {"id": 11, "nome": "Julia Mendes",  "cidade": "Fortaleza"},
    {"id": 12, "nome": "Rafael Costa",  "cidade": "Belo Horizonte"},
]


@app.get("/api/users")
def get_all_users():
    return jsonify(USER_REGISTRY)


if __name__ == "__main__":
    # A aplicação roda na porta 5000, exposta pelo container Docker
    app.run(host="0.0.0.0", port=5000)
