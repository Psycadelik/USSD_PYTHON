"""empty message

Revision ID: 170364c7c400
Revises: 
Create Date: 2019-01-06 13:52:39.715572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '170364c7c400'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session_level',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.String(length=128), nullable=True),
    sa.Column('phone_number', sa.String(length=25), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('session_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone_number', sa.String(length=64), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('pip', sa.String(length=128), nullable=True),
    sa.Column('account', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_table('user')
    op.drop_table('session_level')
    # ### end Alembic commands ###