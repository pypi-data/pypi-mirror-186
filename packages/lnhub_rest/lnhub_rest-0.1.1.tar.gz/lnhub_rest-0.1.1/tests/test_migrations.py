from subprocess import run

import erdiagram
import sqlalchemy as sa
from lndb_setup import InstanceSettings
from lndb_setup._clone import clone_test
from lndb_setup.test import get_package_name
from lndb_setup.test._migrations_unit import (
    execute_model_definitions_match_ddl,
    get_migration_config,
    get_migration_id_from_scripts,
)
from pytest_alembic.executor import CommandExecutor, ConnectionExecutor
from pytest_alembic.runner import MigrationContext

from lnhub_rest import engine
from lnhub_rest.schema._core import SQLModel  # updated registry in it!
from lnhub_rest.schema.migrations.settings import PROD_URL
from lnhub_rest.schema.migrations.utils import include_name

schema_package_loc = f"{get_package_name()}/schema"


def get_migration_context(schema_package_loc):
    src_settings = InstanceSettings(
        storage_root="teststore",
        db=PROD_URL,
        name="testdb",
        owner="testuser1",
    )
    connection_string = clone_test(src_settings=src_settings)
    engine = sa.create_engine(connection_string)
    target_metadata = SQLModel.metadata
    config = get_migration_config(
        schema_package_loc,
        target_metadata,
        include_schemas=True,
        include_name=include_name,
    )
    command_executor = CommandExecutor.from_config(config)
    command_executor.configure(connection=engine)
    migration_context = MigrationContext.from_config(
        config, command_executor, ConnectionExecutor(), engine
    )
    return migration_context


def test_model_definitions_match_ddl_postgres():
    migration_context = get_migration_context(schema_package_loc)
    execute_model_definitions_match_ddl(migration_context)
    run("docker stop pgtest && docker rm pgtest", shell=True)


def test_export_schema():
    migration_id = get_migration_id_from_scripts(schema_package_loc)
    metadata = sa.MetaData(bind=engine)
    metadata.reflect()
    graph = erdiagram.create_schema_graph(
        metadata=metadata,
        show_datatypes=False,
        show_indexes=False,
        rankdir="LR",
        concentrate=True,
    )
    try:
        graph.write_svg(f"./docs/_schemas/lnhub-schema-{migration_id}.svg")
    except FileNotFoundError:
        print("Did not write schema graph.")
