from datetime import datetime

from pydantic import BaseModel, validator, constr, conint


class OrderBase(BaseModel):
    address: constr(max_length=100)
    date: datetime

    @validator("date")
    def ensure_date_range(cls, value):
        if not datetime(year=1980, month=1, day=1) <= value < datetime(year=2000, month=1, day=1):
            raise ValueError("Must be in range")
        return value


class Order(OrderBase):
    id: int
    status: conint(gt=0, lt=5)

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    class Config:
        orm_mode = True


class OrderUpdate(BaseModel):
    status: conint(gt=0, lt=5)

    class Config:
        orm_mode = True
