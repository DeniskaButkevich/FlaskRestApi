from pydantic import BaseModel, constr, EmailStr


class UserBase(BaseModel):
    fullname: constr(max_length=100)  # https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
    username: constr(max_length=20)


class User(UserBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    email: EmailStr
    password: constr(max_length=50)

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    pass
