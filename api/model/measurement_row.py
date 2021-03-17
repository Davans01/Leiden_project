from api.database import db


class MeasurementRow(db.Model):
    measurement_id = db.Column(
        db.Integer(), db.ForeignKey("measurement.id"), primary_key=True
    )
    measurement = db.relationship("Measurement", back_populates="rows")
    type_id = db.Column(
        db.Integer(), db.ForeignKey("measure_type.id"), primary_key=True
    )
    value = db.Column(db.Float(), nullable=False)
    type = db.relationship("MeasureType")

    def to_dict(self):
        return {
            "value": self.value,
            "type": self.measure_type.to_dict(),
        }
