from datetime import datetime

from api.database import db


class Measurement(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    timestamp = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now().astimezone()
    )
    device_id = db.Column(db.String(), db.ForeignKey("device.serial"), nullable=False)
    device = db.relationship("Device", back_populates="measurements")
    rows = db.relationship("MeasurementRow", back_populates="measurement")

    def to_dict(self):
        return {
            "timestamp": self.timestamp.astimezone().isoformat(),
            "device": self.device_id,
            "rows": [row.to_dict() for row in self.rows],
        }
