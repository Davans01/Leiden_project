"""empty message

Revision ID: 2faf53f8786b
Revises: 0a6c7bde370e
Create Date: 2021-04-14 10:41:09.257119

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2faf53f8786b"
down_revision = "0a6c7bde370e"
branch_labels = None
depends_on = None


measure_type_table = sa.sql.table(
    "measure_type",
    sa.sql.column("id", sa.Integer),
    sa.sql.column("label", sa.String),
    sa.sql.column("dimension_symbol", sa.String),
    sa.sql.column("dimension_name", sa.String),
    sa.sql.column("unit_symbol", sa.String),
    sa.sql.column("unit_name", sa.String),
)


def upgrade():
    op.bulk_insert(
        measure_type_table,
        [
            {
                "id": 1,
                "label": "Air temperature",
                "dimension_symbol": "T",
                "dimension_name": "Temperature",
                "unit_symbol": "°C",
                "unit_name": "Celsius",
            },
            {
                "id": 2,
                "label": "Air humidity",
                "dimension_symbol": "Φ",
                "dimension_name": "Humidity",
                "unit_symbol": "%",
                "unit_name": "Percent",
            },
            {
                "id": 3,
                "label": "Ground temperature 1",
                "dimension_symbol": "T",
                "dimension_name": "Temperature",
                "unit_symbol": "°C",
                "unit_name": "Celsius",
            },
            {
                "id": 4,
                "label": "Ground temperature 2",
                "dimension_symbol": "T",
                "dimension_name": "Temperature",
                "unit_symbol": "°C",
                "unit_name": "Celsius",
            },
            {
                "id": 5,
                "label": "Ground temperature 3",
                "dimension_symbol": "T",
                "dimension_name": "Temperature",
                "unit_symbol": "°C",
                "unit_name": "Celsius",
            },
            {
                "id": 6,
                "label": "Ground humidity",
                "dimension_symbol": "Φ",
                "dimension_name": "Humidity",
                "unit_symbol": "%",
                "unit_name": "Percent",
            },
        ],
    )


def downgrade():
    pass
