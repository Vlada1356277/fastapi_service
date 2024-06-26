"""add device_type

Revision ID: 370d711d6a3d
Revises: b5726cef210b
Create Date: 2024-06-05 19:53:30.482055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '370d711d6a3d'
down_revision: Union[str, None] = 'b5726cef210b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devices', sa.Column('device_type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('devices', 'device_type')
    # ### end Alembic commands ###
