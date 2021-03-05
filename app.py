import os

from flask import Flask
from flask_cors import CORS

import api.bp.status
import api.bp.test
import api.model.test
from api.database import db, migrate

cors = CORS(origins="*")


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = app.config["ENV"] != "production"

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api.bp.status.blueprint)
    app.register_blueprint(api.bp.test.blueprint)

    return app
