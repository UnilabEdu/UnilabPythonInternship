"""Initial Migration

Revision ID: 16490939099a
Revises: 
Create Date: 2022-07-14 22:51:56.475532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16490939099a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=30), nullable=False),
    sa.Column('age', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
