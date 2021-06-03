"""empty message

Revision ID: 525d0986104b
Revises: 0006dc5906ec
Create Date: 2021-05-06 22:34:02.492513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '525d0986104b'
down_revision = '0006dc5906ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('confirmed_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('confirmed_at')
        batch_op.drop_column('active')

    # ### end Alembic commands ###
