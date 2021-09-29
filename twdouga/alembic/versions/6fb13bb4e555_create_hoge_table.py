"""create hoge table

Revision ID: 6fb13bb4e555
Revises: 
Create Date: 2021-09-30 03:24:38.117563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fb13bb4e555'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('request', sa.Column('thumbnail_url', sa.String(length=512)))

def downgrade():
    op.drop_column('request', 'thumbnail_url')
