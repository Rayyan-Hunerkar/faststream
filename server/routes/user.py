from fastapi import APIRouter, Depends, Response
from fastapi_jwt_auth import AuthJWT

from server.models import User, UserOut, UserUpdate
from server.utils.current_user import current_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("", response_model=UserOut)
async def get_user(user: User = Depends(current_user)):
    return user


@router.patch("", response_model=UserOut)
async def update_user(update: UserUpdate, user: User = Depends(current_user)):
    user = user.copy(update=update.dict(exclude_unset=True))
    await user.save()
    return user


@router.delete("")
async def delete_user(auth: AuthJWT = Depends()):
    auth.jwt_required()
    await User.find_one(User.email == auth.get_jwt_subject()).delete()
    return Response(status_code=204)
