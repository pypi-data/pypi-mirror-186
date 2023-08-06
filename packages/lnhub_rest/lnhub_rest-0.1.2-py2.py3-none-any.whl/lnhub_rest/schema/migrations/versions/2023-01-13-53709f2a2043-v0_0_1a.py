"""v0.0.1a.

Revision ID: 53709f2a2043
Revises:
Create Date: 2023-01-13 21:35:46.307493

"""
import sqlalchemy as sa  # noqa
import sqlmodel  # noqa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "53709f2a2043"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # rename schema column to schema_str as schema isn't possible with pydantic
    op.alter_column("instance", column_name="schema", new_column_name="schema_str")

    # fix a few internals
    op.alter_column(
        "instance",
        "time_created",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )
    op.create_index(
        op.f("ix_instance_time_created"), "instance", ["time_created"], unique=False
    )
    op.create_index(
        op.f("ix_instance_time_updated"), "instance", ["time_updated"], unique=False
    )

    op.alter_column(
        "usermeta",
        "time_created",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )
    op.drop_constraint("usermeta_handle_key", "usermeta", type_="unique")
    op.drop_constraint("usermeta_lnid_key", "usermeta", type_="unique")
    op.create_index(op.f("ix_usermeta_handle"), "usermeta", ["handle"], unique=True)
    op.create_index(op.f("ix_usermeta_id"), "usermeta", ["id"], unique=False)
    op.create_index(op.f("ix_usermeta_lnid"), "usermeta", ["lnid"], unique=True)
    op.create_index(
        op.f("ix_usermeta_time_created"), "usermeta", ["time_created"], unique=False
    )
    op.create_index(
        op.f("ix_usermeta_time_updated"), "usermeta", ["time_updated"], unique=False
    )


def downgrade() -> None:
    pass
