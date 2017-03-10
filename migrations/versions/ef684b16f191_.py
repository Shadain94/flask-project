"""empty message

Revision ID: ef684b16f191
Revises: 
Create Date: 2017-03-10 14:20:50.151557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef684b16f191'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('username', sa.String(length=12), nullable=True),
    sa.Column('age', sa.String(length=10), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###