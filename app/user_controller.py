from flask import Flask, jsonify, request
from user import db, User
from user_service import UserService, UserRepository
from configDB import url

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

user_service = UserService(UserRepository())

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'username' not in data or 'email' not in data:
        return jsonify({'message': 'Missing username or email'}), 400
    user = user_service.create_user(data['username'], data['email'])
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201

if __name__ == '__main__':
    app.run(debug=True)

