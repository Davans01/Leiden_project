from api.database import db


class Device(db.Model):
    serial = db.Column(db.String(), primary_key=True)
    pairing_code = db.Column(db.String(), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    user = db.relation("User", back_populates="devices")
    measurements = db.relationship("Measurement", back_populates="device")

    def to_dict(self):
        return {
            "serial": self.serial,
            "pairingCode": self.pairing_code,
        }
