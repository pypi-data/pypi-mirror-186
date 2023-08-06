from fastapi import APIRouter

from .utils import get_account_by_id, supabase_client

router = APIRouter(prefix="/user")


@router.get("/profile/{user_id}")
def get_profile(user_id: str):
    usermeta = get_account_by_id(user_id)
    if usermeta is None:
        return None
    profile_picture_url = get_profile_picture_url(user_id)
    return {**usermeta, "profile_picture_url": profile_picture_url}


@router.get("/picture/{user_id}")
def get_profile_picture_url(user_id: str):
    try:
        data = (
            supabase_client.storage()
            .from_("storage-user-hub")
            .create_signed_url(f"{user_id}/profile-picture", 3600)
        )
        return data["signedURL"]
    except Exception:
        return None
