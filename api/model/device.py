from api.database import db


class Device(db.Model):
    serial = db.Column(db.String(), primary_key=True)
    pairing_code = db.Column(db.String(), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    user = db.relation("User", back_populates="devices")

    def serialize(self):
        return {
            "serial": self.serial,
            "pairing_code": self.pairing_code,
        }
