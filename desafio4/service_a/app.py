from flask import Flask, jsonify

app = Flask(__name__)

# Conjunto estático de usuários apenas para demonstração (simulando um "banco" em memória)
USERS_DATASET = [
    {"id": 101, "nome": "Ana Souza",   "status": "ativo",   "registro": "2022-09-10"},
    {"id": 102, "nome": "Bruno Lima",  "status": "inativo", "registro": "2023-02-01"},
    {"id": 103, "nome": "Carlos Silva","status": "ativo",   "registro": "2024-01-18"},
]


def carregar_usuarios():
    """
    Função auxiliar que encapsula a origem dos dados.
    Em um cenário real, aqui poderíamos acessar um banco de dados.
    """
    return USERS_DATASET


@app.get("/usuarios")
def listar_usuarios():
    """
    Endpoint responsável por devolver a lista de usuários em formato JSON.
    Não recebe parâmetros e apenas serializa os dados mockados.
    """
    usuarios = carregar_usuarios()
    return jsonify(usuarios)


if __name__ == "__main__":
    # Executa o serviço Flask escutando em todas as interfaces na porta 5000
    app.run(host="0.0.0.0", port=5000)
