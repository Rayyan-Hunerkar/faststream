import os
from pathlib import Path

import environ
import pydantic

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
env = environ.Env()
ENVIRONMENT = os.environ.get('ENV')
print('ENVIRONMENT->', ENVIRONMENT)
env_config = {
    f'{ENVIRONMENT}': f'{BASE_DIR}/environments/.env.{ENVIRONMENT}'
}
print(env_config.get(ENVIRONMENT))
file_path = env_config.get(ENVIRONMENT)

if file_path:
    environ.Env.read_env(os.path.join(BASE_DIR, file_path))
else:
    print(f"ENV: {ENVIRONMENT} is unhandled!")


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = file_path


class APISettings(BaseSettings):
    title: str = env('API_TITLE')
    host: str = env('API_HOST')
    port: int = env('API_PORT')
    log_level: str = env('API_LOG_LEVEL')

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class MongoSettings(BaseSettings):
    uri: str = env('MONGO_URI')
    database: str = env('MONGO_DATABASE')

    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"


class JWTSettings(BaseSettings):
    authjwt_secret_key: str = env("JWT_SECRET_KEY")
    authjwt_algorithm: str = env("JWT_ALGORITHM")
    authjwt_access_token_expires: str = env("JWT_TOKEN_EXPIRY")

    class Config(BaseSettings.Config):
        env_prefix = "JWT_"


class Salt(BaseSettings):
    salt: str = env("SALT")

    class config(BaseSettings.Config):
        env_prefix = "SALT"


apisettings = APISettings()
mongosettings = MongoSettings()
jwtsettings = JWTSettings()
salt = Salt()