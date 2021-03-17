"""empty message

Revision ID: 36fc3380d597
Revises: 127a344403cf
Create Date: 2021-03-17 15:43:39.742630

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "36fc3380d597"
down_revision = "127a344403cf"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "measurement_row",
        sa.Column("measurement_id", sa.Integer(), nullable=False),
        sa.Column("type_id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["measurement_id"],
            ["measurement.id"],
        ),
        sa.ForeignKeyConstraint(
            ["type_id"],
            ["measure_type.id"],
        ),
        sa.PrimaryKeyConstraint("measurement_id", "type_id"),
    )


def downgrade():
    op.drop_table("measurement_row")
