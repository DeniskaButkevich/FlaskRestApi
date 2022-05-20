from typing import List
from datetime import datetime

from pydantic import BaseModel, validator, constr, conint

from core.schemas.product import Product


class OrderBase(BaseModel):
    address: constr(max_length=100)


class Order(OrderBase):
    id: int
    status: conint(gt=0, lt=5)
    products: List[Product]
    user_id: int
    date: datetime

    @validator("date")
    def ensure_date_range(cls, value):
        if not datetime(year=1980, month=1, day=1) <= value < datetime(year=2023, month=1, day=1):
            raise ValueError("Must be in range")
        return value

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    product_ids: list[int]
    user_id: int

    class Config:
        orm_mode = True


class OrderUpdate(BaseModel):
    status: conint(gt=0, lt=5)

    class Config:
        orm_mode = True
