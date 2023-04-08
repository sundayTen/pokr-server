from enum import Enum, auto

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class PeriodCategory(Enum):
    WEEK = auto()
    MONTH = auto()
