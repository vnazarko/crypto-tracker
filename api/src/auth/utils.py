from datetime import timedelta, datetime

import bcrypt
import jwt
from fastapi import Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer
from jwt import ExpiredSignatureError, InvalidTokenError

from src.config import settings
from src.database import users_collection
from src.auth.schemas import UserSchema


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='/auth/login'
)


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
        token: str | bytes,
        public_key: str = settings.auth_jwt.public_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm
) -> dict:
    decoded = jwt.decode(
        jwt=token,
        key=public_key,
        algorithms=[algorithm]
    )

    return decoded


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()

    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password
    )


async def validate_auth_user(
        username: str = Form(),
        password: str = Form()
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid username or password',
    )

    user = await users_collection.find_one({'username': username})

    if not user:
        raise unauthed_exc

    if not validate_password(password=password, hashed_password=user['password']):
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


async def get_current_auth_user(
        payload: dict = Depends(get_current_token_payload)
) -> UserSchema:
    user_id: int = payload.get('sub')

    if user := await users_collection.find_one({'id': user_id}):
        return UserSchema(
            id=user['id'],
            username=user['username'],
            first_name=user['first_name'],
            photo_url=user['photo_url'],
            password=user['password'],
            active=user['active'],
        )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Token invalid',
    )


def get_current_active_auth_user(
        user: UserSchema = Depends(get_current_auth_user)
):
    if user.active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='User is inactive',
    )