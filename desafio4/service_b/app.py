import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# URL do serviço de usuários (Serviço A), obtida por variável de ambiente
SERVICE_A_URL = os.environ.get(
    "SERVICE_A_URL",
    "http://service-a:5000/usuarios"
)


@app.route("/info", methods=["GET"])
def aggregate_user_info():
    """Consulta o Serviço A e retorna as informações formatadas para o cliente."""
    try:
        # Chamada HTTP ao microsserviço de usuários
        response = requests.get(SERVICE_A_URL)
        response.raise_for_status()

        users = response.json()

        formatted_users = []
        for user in users:
            status_legivel = "Ativo" if user.get("status") == "ativo" else "Inativo"
            info_str = (
                f"Usuário {user.get('nome')} | "
                f"Status: {status_legivel} | "
                f"Registrado em: {user.get('registro')}"
            )
            formatted_users.append(info_str)

        return jsonify(
            {
                "status": "ok",
                "usuarios_formatados": formatted_users,
                "origem_dados": SERVICE_A_URL,
            }
        )

    except requests.exceptions.ConnectionError:
        return (
            jsonify(
                {
                    "status": "erro",
                    "mensagem": "Não foi possível se conectar ao Serviço de Usuários (Serviço A).",
                }
            ),
            503,
        )
    except Exception as exc:
        return jsonify({"status": "erro", "mensagem": str(exc)}), 500


if __name__ == "__main__":
    # Executa na porta 5001 para não conflitar com o Serviço A
    app.run(host="0.0.0.0", port=5001)
