"""updated_email_check

Revision ID: 5d5d23171c62
Revises: ace4f183072f
Create Date: 2026-07-23 16:31:02.457992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d5d23171c62'
down_revision: Union[str, Sequence[str], None] = 'ace4f183072f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    
    op.drop_constraint(
        constraint_name="ck_email_valid_email",
        table_name="user"
    )

    op.create_check_constraint(
        constraint_name="ck_user_valid_email",
        table_name="user",
        condition=sa.text("email ~* \'^[A-Za-z0-9._%%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$\'")
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        constraint_name="ck_user_valid_email",
        table_name="user"
    )
    
    op.create_check_constraint(
        constraint_name="ck_email_valid_email",
        table_name="user",
        condition=sa.text("email ~* \'^[A-Za-z0-9._%%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$\'")
    )
