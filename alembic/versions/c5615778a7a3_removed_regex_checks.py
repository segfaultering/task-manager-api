"""Removed regex checks

Revision ID: c5615778a7a3
Revises: 5d5d23171c62
Create Date: 2026-07-23 21:01:22.139488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5615778a7a3'
down_revision: Union[str, Sequence[str], None] = '5d5d23171c62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint(
        constraint_name="ck_user_valid_email",
        table_name="user"
    )
    op.drop_constraint(
        constraint_name="ck_user_valid_username",
        table_name="user"
    )

    op.drop_constraint(
        constraint_name="ck_task_user_valid_taskname",
        table_name="task"
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.create_check_constraint(
        constraint_name="ck_task_user_valid_taskname",
        table_name="task",
        condition=sa.text("name ~* \'^[A-Za-z0-9._]+$\'::text")
    )

    op.create_check_constraint(
        constraint_name="ck_user_valid_username",
        table_name="user",
        condition=sa.text("username ~ \'^[A-Za-z0-9._]+$\'::text")
    )

    op.create_check_constraint(
        constraint_name="ck_user_valid_email",
        table_name="user",
        condition=sa.text("email ~* \'^[A-Za-z0-9._%%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$\'::text")
    )

