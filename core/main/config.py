# config.py
from typing import Optional
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    ENV_STATE: Optional[str] = Field("dev", env="ENV_STATE")


class Dev(Settings):
    PORT = 8000

    ENV_STATE = "dev"  # or prod

    DB_USER = "admin"
    DB_PASS = "admin"
    DB_NAME = "fast_db_test"
    DB_HOST = "localhost"


class Prod(Settings):
    pass


class Test(Settings):
    PORT = 5000

    ENV_STATE = "test"  # or prod

    DB_USER = "docker"
    DB_PASS = "docker"
    DB_NAME = "fast_db"
    DB_HOST = "db"


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
