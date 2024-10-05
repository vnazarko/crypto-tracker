from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

from src.auth.schemas import TokenInfo, UserSchema
from src.database import users_collection
from src.auth.utils import get_current_active_auth_user, encode_jwt, validate_auth_user, hash_password

router = APIRouter(prefix='/auth', tags=['Auth'])


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
        'password': hash_password(user.password),
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

    jwt_payload = {
        'sub': user['id'],
    }

    access_token = encode_jwt(jwt_payload)

    return TokenInfo(
        access_token=access_token,
        token_type='Bearer'
    )


@router.get('/users/me')
def auth_user_check_info(
        user: UserSchema = Depends(get_current_active_auth_user)
):
    return {
        'username': user.username
    }