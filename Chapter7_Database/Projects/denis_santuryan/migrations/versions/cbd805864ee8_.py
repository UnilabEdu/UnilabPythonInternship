"""empty message

Revision ID: cbd805864ee8
Revises: 931bfbc441b8
Create Date: 2021-04-11 10:23:23.763193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbd805864ee8'
down_revision = '931bfbc441b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('test_column')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test_column', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
