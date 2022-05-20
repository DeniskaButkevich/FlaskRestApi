from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session

from core import models
from core.schemas import user as schemas
from core.main.database import get_db

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get("/{id_user}", response_model=schemas.User, status_code=status.HTTP_200_OK)
def get_user(id_user, db: Session = Depends(get_db)):
    return if_exist_user(id_user, db)


@router.get("/", response_model=list[schemas.User], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user_username = db.query(models.User).filter_by(username=user.username).first()
    if db_user_username:
        raise HTTPException(status_code=409, detail="User username taken..")
    db_user_email = db.query(models.User).filter_by(email=user.email).first()
    if db_user_email:
        raise HTTPException(status_code=409, detail="User email taken..")

    db_user = models.User(fullname=user.fullname, username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    return db_user


@router.put("/{id_user}", response_model=schemas.User, status_code=status.HTTP_202_ACCEPTED)
def update_user(user: schemas.UserCreate, id_user: int, db: Session = Depends(get_db)):
    db_user = if_exist_user(id_user, db)

    if user.fullname:
        db_user.fullname = user.fullname
    db.commit()
    return db_user


@router.delete("/{id_user}", response_model=schemas.User, status_code=status.HTTP_200_OK)
def delete_user( id_user, db: Session = Depends(get_db)):
    user = if_exist_user(id_user, db)
    db.delete(user)
    db.commit()
    return


def if_exist_user(id_user, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(id=id_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="Could not find user with that id")
    return user
