"""changed the name of the table

Revision ID: 862317cce17e
Revises: f5ab47cee46c
Create Date: 2021-04-05 21:19:04.704355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '862317cce17e'
down_revision = 'f5ab47cee46c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=True),
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('item_name', sa.VARCHAR(), nullable=True),
    sa.Column('worker_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('orders')
    # ### end Alembic commands ###
