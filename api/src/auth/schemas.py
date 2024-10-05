from pydantic import BaseModel


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


class UserSchema(BaseModel):
    id: int
    username: str | None = None
    first_name: str
    photo_url: str
    password: bytes | str
    active: bool = True