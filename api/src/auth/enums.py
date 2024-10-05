import enum


class JWTTypes(enum.Enum):
    ACCESS = 'access'
    REFRESH = 'refresh'