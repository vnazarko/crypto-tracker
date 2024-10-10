from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.auth.schemas import TokenInfo, UserSchema
from src.database import users_collection
from src.auth.utils.token import create_access_token, create_refresh_token
from src.auth.utils.user import validate_auth_user, get_current_active_auth_user, get_current_auth_user_for_refresh

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
    dependencies=[Depends(http_bearer)]
)


@router.post('/register')
async def register_user(user: UserSchema):
    this_user_exists = await users_collection.find_one({'id': user.id})

    if this_user_exists:
        raise HTTPException(status_code=400, detail='User already exists')

    stmt = users_collection.insert_one({
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'photo_url': user.photo_url,
        'active': user.active
    })

    return JSONResponse(status_code=200, content={
        'status': 'ok',
        'details': 'User created successfully'
    })


@router.post('/login', response_model=TokenInfo)
def auth_user(
        user: UserSchema = Depends(validate_auth_user)
):

    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)

    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post('/refresh', response_model=TokenInfo, response_model_exclude_none=True)
def auth_refresh_token(
        request: Request,
        user: UserSchema = Depends(get_current_auth_user_for_refresh)
):
    access_token = create_access_token(user)

    return TokenInfo(
        access_token=access_token,
    )


@router.get('/users/me')
def auth_user_check_info(
        user: UserSchema = Depends(get_current_active_auth_user)
):
    return {
        'username': user.username
    }


