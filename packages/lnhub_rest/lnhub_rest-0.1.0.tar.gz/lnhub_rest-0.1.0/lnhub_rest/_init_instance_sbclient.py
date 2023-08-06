from typing import Optional
from uuid import uuid4

from pydantic import PostgresDsn

from lnhub_rest._add_storage_sbclient import add_storage
from lnhub_rest._init_instance import validate_schema_arg
from lnhub_rest._sbclient import connect_hub_with_auth


def init_instance(
    *,
    owner: str,  # owner handle
    name: str,  # instance name
    storage: str,  # storage location on cloud
    db: Optional[PostgresDsn] = None,  # DB URI
    schema: Optional[str] = None,  # comma-separated list of schema names
):
    hub = connect_hub_with_auth()

    # get account
    data = hub.table("account").select("*").eq("handle", owner).execute().data
    account = data[0]

    # get storage and add if not yet there
    storage_id = add_storage(storage, account_handle=account["handle"])

    # validate schema arg
    schema_str = validate_schema_arg(schema)

    response = (
        hub.table("instance")
        .select("*")
        .eq("account_id", account["id"])
        .eq("name", name)
        .execute()
    )
    if len(response.data) > 0:
        hub.auth.sign_out()
        return "instance-exists-already"

    instance_fields = {
        "id": uuid4().hex,
        "account_id": account["id"],
        "name": name,
        "storage_id": storage_id,
        "db": db,
        "schema_str": schema_str,
    }
    data = hub.table("instance").insert(instance_fields).execute().data
    assert len(data) == 1
    hub.auth.sign_out()
    return None
