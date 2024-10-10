from pydantic import BaseModel


class SuccessResponse(BaseModel):
    status: str = 'ok'
    payload: str | dict | list