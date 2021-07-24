from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import (jwt_required, get_jwt_identity, get_jwt)
from models import Lent, LentSchema, User

lent = Blueprint('lent', __name__)
    
@lent.route('/lent', methods=['GET'])
@jwt_required()
def get_all_lents():
    lent_schema = LentSchema()
    lents = Lent.query.filter_by(account_id=User.find_by_email(get_jwt_identity()).id).all()
    return lent_schema.dump(lents)

@lent.route('/lent/<id>', methods=['GET'])
@jwt_required()
def get_lent(id):
    lent_schema = LentSchema()
    lent = Lent.query.filter_by(account_id=User.find_by_email(get_jwt_identity()).id, id=id).first()
    return lent_schema.dump(lent)

@lent.route('/lent', methods=['POST'])
@jwt_required()
def add_lent():
    new_lent = Lent(account_id=User.find_by_email(get_jwt_identity()).id, 
                    to=request.json['to'],
                    description=request.json['description'],
                    amount=request.json['amount'],
                    currency=request.json['currency'],
                    due_date=request.json['due_date'])
    try:
        new_lent.save_to_db()
        return jsonify({'message': 'New lent added to database'})
    except:
        return jsonify({'message': 'Something went wrong'}), 500