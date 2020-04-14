"""empty message

Revision ID: 67fdaca2c95a
Revises: 0b3139de028c
Create Date: 2020-04-14 03:08:06.532344

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '67fdaca2c95a'
down_revision = '0b3139de028c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('pic', sa.LargeBinary(), nullable=True))
    op.drop_column('user_profiles', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('image', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.drop_column('user_profiles', 'pic')
    # ### end Alembic commands ###