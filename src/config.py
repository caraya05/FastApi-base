from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = '..envs'
        env_file_encoding = 'utf-8'

    sentry_token: str = None
    authjwt_secret_key: str
    authjwt_access_token_expires: int = 60 * 5  # 5 minutes


# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()


settings = Settings()

auth_scheme = HTTPBearer()
