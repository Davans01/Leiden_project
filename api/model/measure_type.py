from api.database import db


class MeasureType(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    dimension_symbol = db.Column(db.String(), nullable=False)
    dimension_name = db.Column(db.String(), nullable=False)
    unit_symbol = db.Column(db.String(), nullable=False)
    unit_name = db.Column(db.String(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "dimension_symbol": self.dimension_symbol,
            "dimension_name": self.dimension_name,
            "unit_symbol": self.unit_symbol,
            "unit_name": self.unit_name,
        }
