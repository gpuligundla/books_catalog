#app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from app.catalog import main



def create_app(env='dev'):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', env+".py")
    print(configuration)
    app.config.from_pyfile(configuration)
    db.init_app(app)
    app.register_blueprint(main)
    return app