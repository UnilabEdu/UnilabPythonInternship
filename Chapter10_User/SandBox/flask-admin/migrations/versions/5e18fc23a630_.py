"""empty message

Revision ID: 5e18fc23a630
Revises: 4f8f9699a500
Create Date: 2022-07-20 17:02:08.209365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e18fc23a630'
down_revision = '4f8f9699a500'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('country', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'country')
    # ### end Alembic commands ###
