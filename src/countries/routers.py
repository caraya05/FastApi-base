from config import auth_scheme
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from .schemas import Country
from .schemas import CountryCreate
from .utils import create_country
from .utils import get_countries
from .utils import get_country_by_name

router = APIRouter(prefix="/countries", tags=["Countries"])


# Dependency
def get_db(request: Request):
    return request.state.db


@router.post("/countries/", response_model=Country)
async def create_countries(country: CountryCreate, db: Session = Depends(get_db)):
    db_user = get_country_by_name(db, name=country.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return create_country(db=db, country=country)


@router.get("/countries/", response_model=list[Country])
async def read_countries(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    Authorize: AuthJWT = Depends(),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    Authorize.jwt_required()  # This line is required to access this route for jwt token
    users = get_countries(db, skip=skip, limit=limit)
    return users
