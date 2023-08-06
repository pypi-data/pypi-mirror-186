from typing import Optional
from uuid import UUID

import sqlmodel as sqm

from lnhub_rest import engine
from lnhub_rest.schema import Storage


# router /add-storage
def add_storage(root: str, account_id: UUID) -> UUID:
    validate_root_arg(root)
    # check if storage exists already
    stmt = sqm.select(Storage).where(Storage.root == root)
    with sqm.Session(engine) as ss:
        storage = ss.exec(stmt).one_or_none()
    if storage is not None:
        return storage.id

    # add storage
    storage_region = get_storage_region(root)
    storage_type = get_storage_type(root)
    storage = Storage(
        account_id=account_id, root=root, region=storage_region, type=storage_type
    )
    with sqm.Session(engine) as ss:
        ss.add(storage)
        ss.commit()
        ss.refresh(storage)
    return storage.id


def validate_root_arg(root: str) -> None:
    if not root.startswith(("s3://", "gs://")):
        raise ValueError("Only accept s3 and Google Cloud buckets.")


def get_storage_region(storage_root: str) -> Optional[str]:
    storage_root_str = str(storage_root)
    storage_region = None

    if storage_root_str.startswith("s3://"):
        import boto3

        response = boto3.client("s3").get_bucket_location(
            Bucket=storage_root_str.replace("s3://", "")
        )
        # returns `None` for us-east-1
        # returns a string like "eu-central-1" etc. for all other regions
        storage_region = response["LocationConstraint"]
        if storage_region is None:
            storage_region = "us-east-1"

    return storage_region


def get_storage_type(storage_root: str):
    if str(storage_root).startswith("s3://"):
        return "s3"
    elif str(storage_root).startswith("gs://"):
        return "gs"
    else:
        return "local"
