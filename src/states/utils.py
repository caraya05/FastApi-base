from sqlalchemy import cast
from sqlalchemy import String
from sqlalchemy.orm import Session
from states.models import State
from states.schemas import StateCreate


def get_states(db: Session, State_id: str):
    return (
        db.query(State).filter(cast(State.id, String) == cast(State_id, String)).first()
    )


def get_states_by_name(db: Session, name: str):
    return db.query(State).filter(State.name == name).first()


def get_state(db: Session, skip: int = 0, limit: int = 100):
    return db.query(State).offset(skip).limit(limit).all()


def create_state(db: Session, state: StateCreate, country_id: int):
    db_state = State(**state.dict())
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state
