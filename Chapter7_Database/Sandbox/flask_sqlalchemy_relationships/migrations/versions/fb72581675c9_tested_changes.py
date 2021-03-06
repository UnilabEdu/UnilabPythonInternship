"""tested changes

Revision ID: fb72581675c9
Revises: 862317cce17e
Create Date: 2021-04-14 10:48:27.752148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb72581675c9'
down_revision = '862317cce17e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders_orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=True),
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('orders')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('item_name', sa.VARCHAR(), nullable=True),
    sa.Column('worker_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('orders_orders')
    # ### end Alembic commands ###
