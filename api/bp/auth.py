from api.database import db
from api.model.user import User
from flask import Blueprint, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

blueprint = Blueprint("auth", __name__)


@blueprint.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data["email"]
    password = data["password"]
    remember = data["remember"]

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return {"error": "BAD_CREDENTIALS"}, 401

    login_user(user, remember=remember)

    return user.to_dict()


@blueprint.route("/auth/logout", methods=["POST"])
@login_required
def logout():
    logout_user()

    return "", 204


@blueprint.route("/auth/me")
@login_required
def me():
    return current_user.to_dict()


@blueprint.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()

    email = data["email"]
    password = data["password"]

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {"error": "EMAIL_EXISTS"}, 409

    user = User()
    user.email = email
    user.password_hash = generate_password_hash(
        password,
        method="pbkdf2:sha256:1000000",
        salt_length=16,
    )

    db.session.add(user)
    db.session.commit()

    return user.to_dict()
