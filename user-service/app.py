from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = []

@app.route('/')
def home():
    return jsonify({"message": "User Service is running"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid request"}), 400
    user = {
        "id": len(users) + 1,
        "name": data['name'],
        "email": data['email']
    }
    users.append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
