"""empty message

Revision ID: 2992bcc70ed4
Revises: fbb3e41237a7
Create Date: 2021-03-18 17:21:54.501308

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2992bcc70ed4"
down_revision = "fbb3e41237a7"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("measurement", sa.Column("device_id", sa.String(), nullable=False))
    op.drop_constraint("measurement_device_fkey", "measurement", type_="foreignkey")
    op.create_foreign_key(None, "measurement", "device", ["device_id"], ["serial"])
    op.drop_column("measurement", "device")


def downgrade():
    op.add_column(
        "measurement",
        sa.Column("device", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "measurement", type_="foreignkey")
    op.create_foreign_key(
        "measurement_device_fkey", "measurement", "device", ["device"], ["serial"]
    )
    op.drop_column("measurement", "device_id")
