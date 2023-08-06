import os
from urllib.request import urlretrieve

from pydantic import BaseSettings
from supabase import create_client


class Connector(BaseSettings):
    url: str
    key: str


def get_connector_file_url():
    if "LAMIN_ENV" in os.environ:
        if os.environ["LAMIN_ENV"] == "dev":
            return "https://lamin-site-assets.s3.amazonaws.com/connector_dev.env"
        elif os.environ["LAMIN_ENV"] == "test":
            return "https://lamin-site-assets.s3.amazonaws.com/connector_test.env"
        elif os.environ["LAMIN_ENV"] == "staging":
            return "https://lamin-site-assets.s3.amazonaws.com/connector_staging.env"
    return "https://lamin-site-assets.s3.amazonaws.com/connector.env"


def get_lamin_site_base_url():
    if "LAMIN_ENV" in os.environ:
        if os.environ["LAMIN_ENV"] == "dev":
            return "http://localhost:3000"
        elif os.environ["LAMIN_ENV"] == "test":
            return "http://localhost:3000"
        elif os.environ["LAMIN_ENV"] == "staging":
            return "https://staging.lamin.ai"
    return "https://lamin.ai"


def connect_hub():
    file_url = get_connector_file_url()
    connector_file, _ = urlretrieve(file_url)
    connector = Connector(_env_file=connector_file)
    return create_client(connector.url, connector.key)


def connect_hub_with_auth():
    from lndb_setup._settings_load import load_or_create_user_settings

    hub = connect_hub()
    user_settings = load_or_create_user_settings()
    session = hub.auth.sign_in(
        email=user_settings.email, password=user_settings.password
    )
    hub.postgrest.auth(session.access_token)
    return hub
