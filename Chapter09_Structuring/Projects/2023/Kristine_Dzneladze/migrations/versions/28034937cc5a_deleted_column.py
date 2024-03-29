"""deleted column

Revision ID: 28034937cc5a
Revises: bbe5aae23218
Create Date: 2023-01-15 22:54:00.354284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28034937cc5a'
down_revision = 'bbe5aae23218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_column('img_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_name', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
