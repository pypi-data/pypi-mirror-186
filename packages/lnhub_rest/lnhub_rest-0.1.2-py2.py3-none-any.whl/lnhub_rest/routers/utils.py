from .._sbclient import connect_hub

supabase_client = connect_hub()


def get_account_by_id(user_id: str):
    data = supabase_client.table("account").select("*").eq("id", user_id).execute().data
    if len(data) > 0:
        return data[0]
    else:
        return None
