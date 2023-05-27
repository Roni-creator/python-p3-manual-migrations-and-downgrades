"""Renaming students to scholars

Revision ID: 20fbcb09bf81
Revises: 791279dd0760
Create Date: 2023-05-27 15:03:41.011618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20fbcb09bf81'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')


