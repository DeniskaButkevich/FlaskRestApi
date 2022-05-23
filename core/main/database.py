from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import cnf

db_user = cnf.DB_USER
db_pass = cnf.DB_PASS
db_name = cnf.DB_NAME
db_host = cnf.DB_HOST

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
