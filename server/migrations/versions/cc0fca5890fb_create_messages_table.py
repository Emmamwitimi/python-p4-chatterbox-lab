"""Create messages table

Revision ID: cc0fca5890fb
Revises: f8c465cd0b89
Create Date: 2024-10-06 14:35:31.985099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc0fca5890fb'
down_revision = 'f8c465cd0b89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'updated_at')
    # ### end Alembic commands ###
