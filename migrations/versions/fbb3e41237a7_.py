"""empty message

Revision ID: fbb3e41237a7
Revises: 36fc3380d597
Create Date: 2021-03-18 14:33:50.378480

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "fbb3e41237a7"
down_revision = "36fc3380d597"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("measurement", sa.Column("timestamp", sa.DateTime(), nullable=False))


def downgrade():
    op.drop_column("measurement", "timestamp")
