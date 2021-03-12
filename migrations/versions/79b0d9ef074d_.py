"""empty message

Revision ID: 79b0d9ef074d
Revises: e5349a5aab6d
Create Date: 2021-03-12 15:40:29.957140

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "79b0d9ef074d"
down_revision = "e5349a5aab6d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "measure_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("dimension_symbol", sa.String(), nullable=False),
        sa.Column("dimension_name", sa.String(), nullable=False),
        sa.Column("unit_symbol", sa.String(), nullable=False),
        sa.Column("unit_name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "device",
        sa.Column("serial", sa.String(), nullable=False),
        sa.Column("pairing_code", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("serial"),
        sa.UniqueConstraint("pairing_code"),
    )

    op.create_table(
        "measurement",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("type_id", sa.Integer(), nullable=False),
        sa.Column("device", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["device"],
            ["device.serial"],
        ),
        sa.ForeignKeyConstraint(
            ["type_id"],
            ["measure_type.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("measurement")
    op.drop_table("device")
    op.drop_table("measure_type")
