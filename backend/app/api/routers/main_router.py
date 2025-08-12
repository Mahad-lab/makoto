from typing import Any, Dict

from fastapi import APIRouter

from app.api.routers import auth, user
from app.api.routers import oauth2 as social_auth

NOT_FOUND_RESPONSE: Dict[int | str, Dict[str, Any]] = {
    404: {"description": "Not found"}
}

router = APIRouter()

router.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"],
    responses=NOT_FOUND_RESPONSE,
)


router.include_router(
    user.router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


router.include_router(
    social_auth.social_auth_module,
    prefix="/social",
    tags=["social-auth"],
    responses={404: {"description": "Not found"}},
)

