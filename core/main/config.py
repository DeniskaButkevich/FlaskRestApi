# config.py
import os
from typing import Optional
from pydantic import BaseSettings, Field

NAME = os.environ.get('NAME')


class Settings(BaseSettings):
    secret_key: str = Field('random_string', env='ANOTHER_SECRET_KEY')
    port: int = 5050
    username: str = "ANAND"
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    class Config:
        case_sensitive = False
        env_file = '.env' # This is the key factor


class Dev(Settings):
    username = "TRIPATHI"

    class Config:
        env_file = 'dev.env'


class Prod(Settings):
    username = "Production"
    port = 5051

    class Config:
        env_file = 'prod.env'


class Test(Settings):
    username = "Testing"
    port = 5051
    DATABASE_URL = "postgresql://admin:admin@db:5432/fast_db"
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@db:5432/fast_db"

    class Config:
        env_file = 'test.env'


class FactoryConfig:
    """Returns a config instance dependending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return Dev()

        elif self.env_state == "prod":
            return Prod()
        elif self.env_state == "test":
            return Test()


cnf = FactoryConfig(Settings().ENV_STATE)()
print(cnf.__repr__())