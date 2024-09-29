from flask import Blueprint, request, jsonify
from app import db
from app.models import Owner, Car

VALID_COLORS = ['yellow', 'blue', 'gray']
VALID_MODELS = ['hatch', 'sedan', 'convertible']

car_bp = Blueprint('car_bp', __name__)

@car_bp.route('/owners', methods=['GET'])
def get_owners():
    owners = Owner.query.all()
    return jsonify([{"id": owner.id, "name": owner.name} for owner in owners])

@car_bp.route('/owners', methods=['POST'])
def add_owner():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'message': 'Invalid input, name is required'}), 400
    
    new_owner = Owner(name=data['name'])
    db.session.add(new_owner)
    db.session.commit()
    
    return jsonify({'message': 'Owner added successfully'}), 201

@car_bp.route('/owners/<int:owner_id>/cars', methods=['POST'])
def add_car(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    data = request.get_json()

    if len(owner.cars) >= 3:
        return jsonify({'message': 'Owner cannot have more than 3 cars'}), 400

    if data['model'] not in VALID_MODELS:
        return jsonify({'message': f'Invalid model. Choose one of: {", ".join(VALID_MODELS)}'}), 400
    
    if data['color'] not in VALID_COLORS:
        return jsonify({'message': f'Invalid color. Choose one of: {", ".join(VALID_COLORS)}'}), 400

    new_car = Car(model=data['model'], color=data['color'], owner_id=owner.id)
    db.session.add(new_car)
    db.session.commit()
    
    return jsonify({'message': 'Car added successfully'}), 201
