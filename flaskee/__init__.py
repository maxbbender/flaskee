from config import config
from flask import Flask
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()


def createApp(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    config[configName].init_app(app)

    db.init_app(app)
    csrf.init_app(app)
