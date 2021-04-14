from api.database import db


class MeasureType(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    label = db.Column(db.String(), nullable=False, unique=True)
    dimension_symbol = db.Column(db.String(), nullable=False)
    dimension_name = db.Column(db.String(), nullable=False)
    unit_symbol = db.Column(db.String(), nullable=False)
    unit_name = db.Column(db.String(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "dimensionSymbol": self.dimension_symbol,
            "dimensionName": self.dimension_name,
            "unitSymbol": self.unit_symbol,
            "unitName": self.unit_name,
        }
