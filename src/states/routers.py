from countries.utils import get_country
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from sqlalchemy.orm import Session

from .schemas import State
from .schemas import StateCreate
from .utils import create_state
from .utils import get_state
from .utils import get_states_by_name

router = APIRouter(prefix="/states", tags=["States"])


# Dependency
def get_db(request: Request):
    return request.state.db


@router.post("/states/", response_model=State)
async def create_states(state: StateCreate, db: Session = Depends(get_db)):
    db_states_name = get_states_by_name(db, name=state.name)
    db_country_id = get_country(db, country_id=state.country_id)
    if db_states_name:
        raise HTTPException(status_code=400, detail="Name already registered")
    if not db_country_id:
        raise HTTPException(status_code=400, detail="Country not exist")
    return create_state(db=db, state=state, country_id=state.country_id)


@router.get("/states/", response_model=list[State])
async def read_states(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_state(db, skip=skip, limit=limit)
    return users
