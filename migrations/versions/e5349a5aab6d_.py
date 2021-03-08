"""empty message

Revision ID: e5349a5aab6d
Revises: 284d6b71ce16
Create Date: 2021-03-08 12:44:17.403707

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e5349a5aab6d"
down_revision = "284d6b71ce16"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("user", "user_id", new_column_name="id")


def downgrade():
    op.alter_column("user", "id", new_column_name="user_id")
