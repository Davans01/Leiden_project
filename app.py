import os
import secrets

from flask import Flask
from flask_cors import CORS

import api.bp.auth
import api.bp.status
import api.model.user
from api.database import db, migrate
from api.login import login_manager

cors = CORS(origins="http://localhost:8080", supports_credentials=True)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    if not app.config["SECRET_KEY"]:
        app.config["SECRET_KEY"] = secrets.token_bytes(64)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = app.config["ENV"] != "production"

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(api.bp.auth.blueprint)
    app.register_blueprint(api.bp.status.blueprint)

    return app
