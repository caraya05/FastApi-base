from sqlalchemy import cast
from sqlalchemy import String
from sqlalchemy.orm import Session

from .models import Country
from .schemas import CountryCreate


def get_country(db: Session, country_id: str):
    return (
        db.query(Country)
        .filter(cast(Country.id, String) == cast(country_id, String))
        .first()
    )


def get_country_by_name(db: Session, name: str):
    return db.query(Country).filter(Country.name == name).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Country).offset(skip).limit(limit).all()


def create_country(db: Session, country: CountryCreate):
    db_country = Country(
        name=country.name, code=country.code, is_active=country.is_active
    )
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country
