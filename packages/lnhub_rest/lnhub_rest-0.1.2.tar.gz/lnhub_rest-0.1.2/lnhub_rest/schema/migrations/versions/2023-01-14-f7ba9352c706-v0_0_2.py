"""v0.0.2.

Revision ID: f7ba9352c706
Revises: c555c87a640c
Create Date: 2023-01-14 22:42:56.185489

"""
import sqlalchemy as sa  # noqa
import sqlmodel  # noqa
from alembic import op
from sqlalchemy.dialects import postgresql  # noqa

# revision identifiers, used by Alembic.
revision = "f7ba9352c706"
down_revision = "c555c87a640c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("instance")
    op.drop_table("storage")
    op.rename_table("usermeta", "account")
    op.alter_column("account", column_name="time_created", new_column_name="created_at")
    op.alter_column("account", column_name="time_updated", new_column_name="updated_at")
    op.create_table(
        "organization",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"], ["account.id"], name=op.f("fk_organization_id_account")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_organization")),
    )

    op.create_table(
        "storage",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("account_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("root", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("type", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("region", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["account_id"], ["account.id"], name=op.f("fk_storage_account_id_account")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_storage")),
    )
    op.create_index(
        op.f("ix_storage_account_id"), "storage", ["account_id"], unique=False
    )
    op.create_index(
        op.f("ix_storage_created_at"), "storage", ["created_at"], unique=False
    )
    op.create_index(op.f("ix_storage_root"), "storage", ["root"], unique=True)
    op.create_index(
        op.f("ix_storage_updated_at"), "storage", ["updated_at"], unique=False
    )

    op.create_table(
        "instance",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("account_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("storage_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("db", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("schema_str", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["account_id"], ["account.id"], name=op.f("fk_instance_account_id_account")
        ),
        sa.ForeignKeyConstraint(
            ["storage_id"], ["storage.id"], name=op.f("fk_instance_storage_id_storage")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_instance")),
        sa.UniqueConstraint("account_id", "name", name=op.f("uq_instance_account_id")),
    )
    op.create_index(
        op.f("ix_instance_account_id"), "instance", ["account_id"], unique=False
    )
    op.create_index(
        op.f("ix_instance_created_at"), "instance", ["created_at"], unique=False
    )
    op.create_index(
        op.f("ix_instance_storage_id"), "instance", ["storage_id"], unique=False
    )
    op.create_index(
        op.f("ix_instance_updated_at"), "instance", ["updated_at"], unique=False
    )

    op.add_column(
        "account", sa.Column("user_id", sqlmodel.sql.sqltypes.GUID(), nullable=True)
    )
    op.drop_index("ix_usermeta_handle", table_name="account")
    op.drop_index("ix_usermeta_id", table_name="account")
    op.drop_index("ix_usermeta_lnid", table_name="account")
    op.drop_index("ix_usermeta_time_created", table_name="account")
    op.drop_index("ix_usermeta_time_updated", table_name="account")
    op.create_index(
        op.f("ix_account_created_at"), "account", ["created_at"], unique=False
    )
    op.create_index(op.f("ix_account_handle"), "account", ["handle"], unique=True)
    op.create_index(op.f("ix_account_lnid"), "account", ["lnid"], unique=True)
    op.create_index(op.f("ix_account_name"), "account", ["name"], unique=False)
    op.create_index(
        op.f("ix_account_updated_at"), "account", ["updated_at"], unique=False
    )
    op.create_index(op.f("ix_account_user_id"), "account", ["user_id"], unique=False)
    op.drop_constraint("usermeta_id_fkey", "account", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_account_user_id_users"),
        "account",
        "users",
        ["user_id"],
        ["id"],
        referent_schema="auth",
    )

    op.execute("update account set user_id = id")


def downgrade() -> None:
    pass
