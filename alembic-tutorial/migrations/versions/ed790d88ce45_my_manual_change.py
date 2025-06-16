"""my manual change

Revision ID: ed790d88ce45
Revises: 80a1c0f0edca
Create Date: 2025-06-12 11:44:48.460373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed790d88ce45'
down_revision: Union[str, None] = '80a1c0f0edca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("UPDATE users SET password = 'NoPassword' WHERE password IS NULL")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("UPDATE users SET password = '' WHERE password IS NOT NULL")
