from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app import bcrypt, db
from app.models import Owner

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    owner = Owner.query.filter_by(name=data['name']).first()

    if owner and bcrypt.check_password_hash(owner.password, data['password']):
        token = create_access_token(identity=owner.id)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
