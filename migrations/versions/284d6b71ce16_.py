"""empty message

Revision ID: 284d6b71ce16
Revises: e3685395d234
Create Date: 2021-03-08 12:13:03.941353

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "284d6b71ce16"
down_revision = "e3685395d234"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password_hash", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("email"),
    )
    op.drop_table("test")


def downgrade():
    op.create_table(
        "test",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="test_pkey"),
    )
    op.drop_table("user")
