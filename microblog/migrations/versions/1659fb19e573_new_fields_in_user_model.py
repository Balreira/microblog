"""new fields in user model

Revision ID: 1659fb19e573
Revises: 021a3fe1c7d3
Create Date: 2020-03-07 16:26:31.194298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1659fb19e573'
down_revision = '021a3fe1c7d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
