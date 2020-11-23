"""empty message

Revision ID: 5b1da7f439f4
Revises: 92ed4fa15d50
Create Date: 2020-11-23 14:14:41.577297

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5b1da7f439f4'
down_revision = '92ed4fa15d50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reader', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reader', sa.Column('address', mysql.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###
