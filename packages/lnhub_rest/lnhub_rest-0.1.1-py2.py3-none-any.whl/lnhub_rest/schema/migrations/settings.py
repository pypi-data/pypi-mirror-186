import os

try:
    PROD_URL = f"postgresql://postgres:{os.environ['LNHUB_PROD_PG_PASSWORD']}@db.laesaummdydllppgfchu.supabase.co:5432/postgres"  # noqa
except KeyError:
    PROD_URL = "no-admin-password"
