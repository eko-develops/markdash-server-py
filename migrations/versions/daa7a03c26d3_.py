"""empty message

Revision ID: daa7a03c26d3
Revises: 
Create Date: 2023-03-13 17:30:39.798074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daa7a03c26d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('promotion', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_date', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('end_date', sa.String(), nullable=True))
        batch_op.drop_column('schedule_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('promotion', schema=None) as batch_op:
        batch_op.add_column(sa.Column('schedule_date', sa.DATETIME(), nullable=True))
        batch_op.drop_column('end_date')
        batch_op.drop_column('start_date')

    # ### end Alembic commands ###