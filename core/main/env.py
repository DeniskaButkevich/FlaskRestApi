from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    db_name: str
    db_pass: str
    db_url: PostgresDsn
    debug: bool
    seed: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
print(settings)