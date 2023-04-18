import uuid

from database import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


def generate_uuid():
    return str(uuid.uuid4())


class Country(Base):
    __tablename__ = "countries"

    id = Column(String, name="id", primary_key=True, default=generate_uuid, index=True)
    name = Column(String, unique=True, index=True)
    code = Column(String)
    is_active = Column(Boolean, default=True)
    states = relationship('State', back_populates='country')
