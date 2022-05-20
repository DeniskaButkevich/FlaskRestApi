from typing import List

from pydantic import BaseModel, constr

from core.schemas.product import Product


class CategoryBase(BaseModel):
    name: constr(min_length=3, max_length=20)


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    class Config:
        orm_mode = True


class CategoryUpdate(CategoryBase):
    class Config:
        orm_mode = True


class CategoryProducts(CategoryBase):
    products: List[Product]

    class Config:
        orm_mode = True
