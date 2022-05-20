from typing import List

from pydantic import BaseModel, constr


class ProductBase(BaseModel):
    name: constr(min_length=3, max_length=20)
    description: constr(max_length=200)
    price: float


# class CategoryForProduct(BaseModel):
#     id: int
#     name: str


class Product(ProductBase):
    id: int
    # categories: list[CategoryForProduct]

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    class Config:
        orm_mode = True


class ProductUpdate(ProductBase):

    class Config:
        orm_mode = True
