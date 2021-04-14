"""empty message

Revision ID: 0a6c7bde370e
Revises: 2992bcc70ed4
Create Date: 2021-04-14 10:37:42.867012

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0a6c7bde370e"
down_revision = "2992bcc70ed4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("measure_type", sa.Column("label", sa.String(), nullable=False))


def downgrade():
    op.drop_column("measure_type", "label")
