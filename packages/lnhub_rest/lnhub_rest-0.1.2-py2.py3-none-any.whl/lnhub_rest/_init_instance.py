"""Initializing an instance.

This functionality will at first only be accessible through Python API client & CLI.

We might also enable it from the UI.
"""
from typing import Optional

import sqlmodel as sqm
from pydantic import PostgresDsn

from lnhub_rest import engine
from lnhub_rest._add_storage import add_storage
from lnhub_rest._assets import schemas as known_schema_names
from lnhub_rest.schema import Account, Instance


# router /init-instance
def init_instance(
    *,
    owner: str,  # owner handle
    name: str,  # instance name
    storage: str,  # storage location on cloud
    db: Optional[PostgresDsn] = None,  # DB URI
    schema: Optional[str] = None,  # comma-separated list of schema names
) -> Optional[str]:
    # get account
    select_account = sqm.select(Account).where(Account.handle == owner)
    with sqm.Session(engine) as ss:
        account = ss.exec(select_account).one()

    # get storage and add if not yet there
    storage_id = add_storage(storage, account_id=account.id)

    # validate schema arg
    schema_str = validate_schema_arg(schema)

    # check whether instance exists already
    select_instance = sqm.select(Instance).where(
        Instance.account_id == account.id, Instance.name == name
    )
    with sqm.Session(engine) as ss:
        instance = ss.exec(select_instance).one_or_none()
    if instance is not None:
        return "instance-exists-already"

    # add instance
    instance = Instance(
        account_id=account.id,
        name=name,
        storage_id=storage_id,
        db=db,
        schema_str=schema_str,
    )
    with sqm.Session(engine) as ss:
        ss.add(instance)
        ss.commit()

    return None


def validate_schema_arg(schema: Optional[str] = None) -> str:
    if schema is None:
        return ""
    validated_schema = []
    for module in known_schema_names:
        if module in schema:
            validated_schema.append(module)
    if len(validated_schema) == 0:
        raise ValueError(f"Unknown schema modules. Only know {known_schema_names}.")
    return ",".join(validated_schema)
