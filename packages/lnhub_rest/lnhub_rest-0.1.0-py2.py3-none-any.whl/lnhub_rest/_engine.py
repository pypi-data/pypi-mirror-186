from sqlmodel import create_engine

from lnhub_rest.schema.migrations.settings import PROD_URL

if PROD_URL != "no-admin-password":
    engine = create_engine(PROD_URL)  # enqine
else:
    engine = None
