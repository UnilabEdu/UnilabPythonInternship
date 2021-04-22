"""empty message

Revision ID: 755f5ab5afbe
Revises: 
Create Date: 2021-04-21 20:10:36.103313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '755f5ab5afbe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('randoms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('param1', sa.String(), nullable=True),
    sa.Column('param2', sa.String(), nullable=True),
    sa.Column('param3', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_randoms'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('randoms')
    # ### end Alembic commands ###
