from api.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    devices = db.relationship("Device", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
