from fastapi import Form, HTTPException, Depends, status
from jwt import ExpiredSignatureError, InvalidTokenError

from src.auth.enums import JWTTypes
from src.auth.schemas import UserSchema

from src.auth import oauth2_scheme
from src.auth.utils.token import decode_jwt, validate_token_type
from src.database import users_collection


async def validate_auth_user(
        id: int = Form(),
        hash: str = Form(),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid id',
    )

    user = await users_collection.find_one({'id': id})

    if not user:
        raise unauthed_exc

    if not user['active']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='User is inactive',
        )

    return user


def get_current_token_payload(
        token: str = Depends(oauth2_scheme)
) -> dict:
    try:
        payload = decode_jwt(
            token=token
        )
    except ExpiredSignatureError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token',
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token',
        )
    return payload


async def get_user_by_token_sub(payload: dict) -> UserSchema:
    user_id: str | None = payload.get("sub")
    if user := await users_collection.find_one({'id': user_id}):
        return UserSchema(
            username=user['username'],
            first_name=user['first_name'],
            photo_url=user['photo_url'],
            id=user['id'],
            active=user['active'],
        )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid",
    )


def get_auth_user_from_token_of_type(token_type: JWTTypes):
    async def get_auth_user_from_token(
        payload: dict = Depends(get_current_token_payload),
    ) -> UserSchema:
        validate_token_type(payload, token_type)
        return await get_user_by_token_sub(payload)

    return get_auth_user_from_token


get_current_auth_user = get_auth_user_from_token_of_type(JWTTypes.ACCESS.value)
get_current_auth_user_for_refresh = get_auth_user_from_token_of_type(JWTTypes.REFRESH.value)


def get_current_active_auth_user(
        user: UserSchema = Depends(get_current_auth_user)
):
    if user.active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='User is inactive',
    )
