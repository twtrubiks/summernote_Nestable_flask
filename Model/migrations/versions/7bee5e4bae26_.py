"""empty message

Revision ID: 7bee5e4bae26
Revises: None
Create Date: 2016-11-05 20:15:57.131602

"""

# revision identifiers, used by Alembic.
revision = '7bee5e4bae26'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=32), nullable=True),
    sa.Column('Content', sa.String(length=128), nullable=True),
    sa.Column('Parent', sa.Integer(), nullable=True),
    sa.Column('Sequence', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('document')
    ### end Alembic commands ###