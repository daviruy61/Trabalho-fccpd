from flask import Flask, jsonify

app = Flask(__name__)

# Lista estática de pedidos associando usuários e produtos
ORDERS_DATA = [
    {"pedido_id": 5001, "user_id": 10, "produto": "Teclado Mecânico"},
    {"pedido_id": 5002, "user_id": 11, "produto": "Mouse Gamer"},
    {"pedido_id": 5003, "user_id": 10, "produto": "Cadeira Ergonômica"},
]


@app.get("/api/orders")
def list_orders():
    """
    Endpoint responsável por devolver todos os pedidos registrados.
    """
    return jsonify(ORDERS_DATA)


if __name__ == "__main__":
    # Microsserviço de pedidos, exposto na porta 5001
    app.run(host="0.0.0.0", port=5001)
