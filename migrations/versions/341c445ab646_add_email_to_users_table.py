"""add email to users table

Revision ID: 341c445ab646
Revises: cdf84a8ea80f
Create Date: 2019-10-20 18:07:24.840052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '341c445ab646'
down_revision = 'cdf84a8ea80f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
