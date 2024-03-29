"""initial6

Revision ID: cd0f3fc3fa99
Revises: 7b244b9c3c4e
Create Date: 2024-02-06 19:52:42.821069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd0f3fc3fa99'
down_revision = '7b244b9c3c4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('criteria_name', sa.String(length=100), nullable=False),
    sa.Column('best_alternative', sa.Float(), nullable=False),
    sa.Column('performance_score', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['alternative.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    # ### end Alembic commands ###
