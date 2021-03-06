"""empty message

Revision ID: 3036e7b4664f
Revises: e4c9c3fbde44
Create Date: 2020-10-16 10:15:17.901075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3036e7b4664f'
down_revision = 'e4c9c3fbde44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('shows_venue_id_fkey', 'shows', type_='foreignkey')
    op.drop_constraint('shows_artist_id_fkey', 'shows', type_='foreignkey')
    op.create_foreign_key(None, 'shows', 'venues', ['venue_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'shows', 'artists', ['artist_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.create_foreign_key('shows_artist_id_fkey', 'shows', 'artists', ['artist_id'], ['id'])
    op.create_foreign_key('shows_venue_id_fkey', 'shows', 'venues', ['venue_id'], ['id'])
    # ### end Alembic commands ###
