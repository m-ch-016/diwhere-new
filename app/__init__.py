from flask import Flask 
from config import Config 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()

migrate = Migrate()

login = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    login.init_app(app)
    
    CORS(app)
    from app import main 

    app.register_blueprint(main.bp)

    from app import commands
    commands.register(app)
    
    return app