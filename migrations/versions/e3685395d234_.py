"""empty message

Revision ID: e3685395d234
Revises:
Create Date: 2021-03-05 16:03:22.340998

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e3685395d234"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "test",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("test")
