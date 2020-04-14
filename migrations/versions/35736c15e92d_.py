"""empty message

Revision ID: 35736c15e92d
Revises: 1ac4cb5dc1c3
Create Date: 2020-03-26 17:06:49.742646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35736c15e92d'
down_revision = '1ac4cb5dc1c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_profiles_username_key', 'user_profiles', type_='unique')
    op.create_unique_constraint(None, 'user_profiles', ['email'])
    op.drop_column('user_profiles', 'password')
    op.drop_column('user_profiles', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('user_profiles', sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user_profiles', type_='unique')
    op.create_unique_constraint('user_profiles_username_key', 'user_profiles', ['username'])
    # ### end Alembic commands ###