"""empty message

Revision ID: b9c33c9f897e
Revises: 2faf53f8786b
Create Date: 2021-04-14 11:12:56.679860

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b9c33c9f897e"
down_revision = "2faf53f8786b"
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(None, "measure_type", ["label"])


def downgrade():
    op.drop_constraint(None, "measure_type", type_="unique")
