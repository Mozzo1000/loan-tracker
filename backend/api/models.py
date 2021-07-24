from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @staticmethod
    def generate_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return check_password_hash(hash, password)

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
    email = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()

class Lent(db.Model):
    __tablename__ = 'lent'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, nullable=False)
    to = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String, nullable=True)
    lend_date = db.Column(db.Date, nullable=False, default=datetime.datetime.now())
    due_date = db.Column(db.Date, nullable=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class LentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Lent
    id = ma.auto_field()
    account_id = ma.auto_field()
    to = ma.auto_field()
    description = ma.auto_field()
    amount = ma.auto_field()
    currency = ma.auto_field()
    lend_date = ma.auto_field()
    due_date = ma.auto_field()

class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)