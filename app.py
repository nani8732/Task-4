from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# Home route
@app.route('/')
def home():
    return "Welcome to the User API!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    user_id = max(users.keys()) + 1 if users else 1
    users[user_id] = {"name": data['name'], "email": data['email']}
    return jsonify({"id": user_id, "user": users[user_id]}), 201

# PUT - Update existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update({
        "name": data.get("name", users[user_id]["name"]),
        "email": data.get("email", users[user_id]["email"])
    })
    return jsonify({"message": "User updated", "user": users[user_id]})

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": f"User {user_id} deleted"})

if __name__ == '__main__':
    app.run(debug=True)
