from api.database import db
from sqlalchemy.inspection import inspect


class Test(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Test id={self.id!r}>"

    def serialize(self):
        return {column: getattr(self, column) for column in inspect(self).attrs.keys()}
