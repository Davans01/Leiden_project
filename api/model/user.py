from api.database import db
from flask_login import UserMixin
from sqlalchemy.inspection import inspect


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
