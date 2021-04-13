import os
import secrets

from flask import Flask
from flask_cors import CORS

import api.bp.auth
import api.bp.devices
import api.bp.status
import api.bp.ttn
import api.model.device
import api.model.measure_type
import api.model.measurement
import api.model.measurement_row
import api.model.user
from api.database import db, migrate
from api.login import login_manager


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    if not app.config["SECRET_KEY"]:
        app.config["SECRET_KEY"] = secrets.token_bytes(64)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = app.config["ENV"] != "production"

    app.config["TTN_AUTH_KEY"] = os.getenv("TTN_AUTH_KEY")

    cors = CORS(
        origins=(
            ["https://soilsenseeverywhere.nl"]
            if app.config["ENV"] == "production"
            else ["http://localhost:8080"]
        ),
        supports_credentials=True,
    )

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(api.bp.auth.blueprint)
    app.register_blueprint(api.bp.devices.blueprint)
    app.register_blueprint(api.bp.status.blueprint)
    app.register_blueprint(api.bp.ttn.blueprint)

    return app
