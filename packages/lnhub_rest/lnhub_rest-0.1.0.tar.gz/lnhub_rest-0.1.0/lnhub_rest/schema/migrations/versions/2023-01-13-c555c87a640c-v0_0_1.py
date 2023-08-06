"""v0.0.1.

Revision ID: c555c87a640c
Revises: 53709f2a2043
Create Date: 2023-01-13 23:40:12.882732

"""
import sqlalchemy as sa  # noqa
import sqlmodel  # noqa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "c555c87a640c"
down_revision = "53709f2a2043"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "instance",
        "schema_str",
        existing_type=sa.TEXT(),
        type_=sqlmodel.sql.sqltypes.AutoString(),
        nullable=True,
    )
    op.alter_column(
        "storage", "time_created", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    op.create_index(
        op.f("ix_storage_time_created"), "storage", ["time_created"], unique=False
    )
    op.create_index(
        op.f("ix_storage_time_updated"), "storage", ["time_updated"], unique=False
    )


def downgrade() -> None:
    pass
