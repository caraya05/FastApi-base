from uuid import UUID

from pydantic import BaseModel


class StateBase(BaseModel):
    name: str
    code: str
    is_active: bool


class StateCreate(StateBase):
    country_id: UUID


class State(StateCreate):
    id: UUID

    class Config:
        orm_mode = True
