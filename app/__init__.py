import dash
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import os, sys
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = "secrettttt"#os.environ['SECRET_KEY']
BaseConfig = Config()


def create_app():
    #init flask app
    server = Flask(__name__)
    server.config.from_object(BaseConfig)
    mail = Mail(server)
    register_extensions(server)
    register_blueprints(server)
    return server


def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(server)
    login.init_app(server)
    login.login_view = 'main.login'
    migrate.init_app(server, db)


def register_blueprints(server):
    from app.webapp import server_bp
    #from app.errors import bp as errors_bp

    #server.register_blueprint(errors_bp)

    server.register_blueprint(server_bp)
