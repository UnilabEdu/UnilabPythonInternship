"""first relationship

Revision ID: 6da3a8a7c03a
Revises: 59d2c227fce9
Create Date: 2021-04-11 10:02:56.586220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6da3a8a7c03a'
down_revision = '59d2c227fce9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('followers', sa.Integer(), nullable=True),
    sa.Column('topic', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pages')
    # ### end Alembic commands ###
