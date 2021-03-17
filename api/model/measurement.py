from api.database import db


class Measurement(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    device = db.Column(db.String(), db.ForeignKey("device.serial"), nullable=False)
    rows = db.relationship("MeasurementRow", back_populates="measurement")

    def to_dict(self):
        return {
            "device": self.device.to_dict(),
            "rows": [row.to_dict() for row in self.rows],
        }
