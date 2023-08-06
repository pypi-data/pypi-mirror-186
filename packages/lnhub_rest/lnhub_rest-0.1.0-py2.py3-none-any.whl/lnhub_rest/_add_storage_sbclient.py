from uuid import UUID, uuid4

from ._add_storage import get_storage_region, get_storage_type, validate_root_arg
from ._sbclient import connect_hub


def add_storage(root: str, account_handle: str) -> UUID:
    hub = connect_hub()
    validate_root_arg(root)

    # get account
    data = hub.table("account").select("*").eq("handle", account_handle).execute().data
    account = data[0]

    # check if storage exists already
    response = hub.table("storage").select("*").eq("root", root).execute()
    if len(response.data) == 1:
        return response.data[0]["id"]

    # add storage
    storage_region = get_storage_region(root)
    storage_type = get_storage_type(root)
    storage_fields = {
        "id": uuid4().hex,
        "account_id": account["id"],
        "root": root,
        "region": storage_region,
        "type": storage_type,
    }
    response = hub.table("storage").insert(storage_fields).execute()
    assert len(response.data) == 1

    return response.data[0]["id"]
