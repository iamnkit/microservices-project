from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory order storage
orders = []

@app.route('/')
def home():
    return jsonify({"message": "Order Service is running"}), 200

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'item' not in data or 'quantity' not in data:
        return jsonify({"error": "Invalid request"}), 400
    order = {
        "id": len(orders) + 1,
        "item": data['item'],
        "quantity": data['quantity']
    }
    orders.append(order)
    return jsonify(order), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
