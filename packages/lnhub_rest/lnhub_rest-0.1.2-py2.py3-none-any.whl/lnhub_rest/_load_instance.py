from typing import Tuple

import sqlmodel as sqm
from sqlalchemy.exc import NoResultsFound

from lnhub_rest import engine
from lnhub_rest.schema import Account, Instance, Storage


# router /load-instance
def load_instance(*, owner: str, name: str) -> Tuple[Instance, Storage]:
    # get account
    select_account = sqm.select(Account).where(Account.handle == owner)
    with sqm.Session(engine) as ss:
        account = ss.exec(select_account).one()

    # get instance
    select_instance = sqm.select(Instance).where(
        Instance.account_id == account.id, Instance.name == name
    )
    with sqm.Session(engine) as ss:
        try:
            instance = ss.exec(select_instance).one()
        except NoResultsFound:
            raise ValueError("Instance does not exist.")

    # get default storage
    select_storage = sqm.select(Instance).where(Storage.id == instance.storage_id)
    with sqm.Session(engine) as ss:
        storage = ss.exec(select_storage).one()

    return instance, storage
