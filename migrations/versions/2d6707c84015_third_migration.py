"""Third  Migration

Revision ID: 2d6707c84015
Revises: 432609e5f4e0
Create Date: 2021-11-15 02:11:04.091501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d6707c84015'
down_revision = '432609e5f4e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('topic', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'topic')
    # ### end Alembic commands ###