from uuid import UUID

from pydantic import BaseModel
from states.schemas import State


class CountryBase(BaseModel):
    name: str


class CountryCreate(CountryBase):
    code: str
    is_active: bool


class Country(CountryCreate):
    id: UUID
    states: list[State] = []

    class Config:
        orm_mode = True
