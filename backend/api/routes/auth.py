from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, get_jwt_identity, get_jwt)
from models import User, RevokedTokenModel

auth = Blueprint('auth', __name__)
    
@auth.route('/auth/register', methods=['POST'])
def register():
    if not 'email' or not 'password' in request.json:
        abort(422)
    if User.find_by_email(request.json['email']):
        return jsonify({'message': 'Email {} is already in use'.format(request.json['email'])}), 409

    new_user = User(email=request.json['email'], password=User.generate_hash(request.json['password']),
                    first_name=request.json['first_name'])
    try:
        new_user.save_to_db()
        access_token = create_access_token(identity=request.json['email'])
        refresh_token = create_refresh_token(identity=request.json['email'])
        return jsonify({'message': 'Account with email {} was created'.format(request.json['email']),
                        'access_token': access_token, 'refresh_token': refresh_token}), 201
    except:
        return jsonify({'message': 'Something went wrong'}), 500

@auth.route('/auth/login', methods=['POST'])
def login():
    if not 'email' or not 'password' in request.json:
        abort(422)
    current_user = User.find_by_email(request.json['email'])
    if not current_user:
        return jsonify({'message': 'Wrong email or password, please try again.'}), 404

    if User.verify_hash(request.json['password'], current_user.password):
        access_token = create_access_token(identity=request.json['email'])
        refresh_token = create_refresh_token(identity=request.json['email'])

        return jsonify({'logged_in_as': current_user.email, 'display_name': current_user.first_name,
                        'access_token': access_token, 'refresh_token': refresh_token}), 201
    else:
        return jsonify({'message': 'Wrong username or password, please try again.'}), 401

@auth.route('/auth/refresh', methods=['POST'])
def token_refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify({'access_token': access_token}), 201

@auth.route('/auth/logout/access', methods=['POST'])
@jwt_required()
def user_logout_access():
    jti = get_jwt()['jti']
    try:
        revoked_token = RevokedTokenModel(jti=jti)
        revoked_token.add()
        return jsonify({'message': 'Access token has been revoked'}), 201
    except:
        return jsonify({'message': 'Something went wrong'}), 500


@auth.route('/auth/logout/refresh', methods=['POST'])
@jwt_required(refresh=True)
def user_logout_refresh():
    jti = get_jwt()['jti']
    try:
        revoked_token = RevokedTokenModel(jti=jti)
        revoked_token.add()
        return jsonify({'message': 'Refresh token has been revoked'}), 201
    except:
        return jsonify({'message': 'Something went wrong'}), 500