from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth import auth
import config
from models import db, ma

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
db.init_app(app)
ma.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth, url_prefix='/v1')

@app.route('/', methods=['GET'])
def index():
    return "<h1>Hello world123!</h1>"