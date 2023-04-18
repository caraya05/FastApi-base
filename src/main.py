import sentry_sdk
from config import settings
from countries import models as country_base
from countries import routers as country_routers
from database import engine
from database import SessionLocal
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from states import routers as state_routers

app = FastAPI(
    title="FastAPI Base_",
    description="simple rest-full api with fastapi",
    version="1.0",
)


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(country_routers.router)
app.include_router(state_routers.router)

country_base.Base.metadata.create_all(bind=engine)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    if exc.message == "Signature has expired":
        return JSONResponse(status_code=401, content={"detail": exc.message})
    elif exc.message == "Signature verification failed":
        return JSONResponse(status_code=401, content={"detail": exc.message})

    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.get("/")
async def root():
    return {"message": "FastApi Base API"}


if settings.sentry_token:
    sentry_sdk.init(
        dsn=settings.sentry_token,
        traces_sample_rate=1.0,
    )
