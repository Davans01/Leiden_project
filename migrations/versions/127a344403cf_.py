"""empty message

Revision ID: 127a344403cf
Revises: 79b0d9ef074d
Create Date: 2021-03-17 13:33:15.052524

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "127a344403cf"
down_revision = "79b0d9ef074d"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint("measurement_type_id_fkey", "measurement", type_="foreignkey")
    op.drop_column("measurement", "type_id")
    op.drop_column("measurement", "value")


def downgrade():
    op.add_column(
        "measurement",
        sa.Column(
            "value",
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "measurement",
        sa.Column("type_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "measurement_type_id_fkey", "measurement", "measure_type", ["type_id"], ["id"]
    )
