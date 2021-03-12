from api.database import db


class Measurement(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    value = db.Column(db.Float(), nullable=False)
    type_id = db.Column(db.Integer(), db.ForeignKey("measure_type.id"), nullable=False)
    type = db.relationship("MeasureType")
    device = db.Column(db.String(), db.ForeignKey("device.serial"), nullable=False)

    def serialize(self):
        return {
            "value": self.value,
            "type": self.measure_type.serialize(),
        }
