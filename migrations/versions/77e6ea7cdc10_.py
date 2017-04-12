"""empty message

Revision ID: 77e6ea7cdc10
Revises: 
Create Date: 2017-04-11 17:49:47.683000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77e6ea7cdc10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cityname', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cityname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    # ### end Alembic commands ###
