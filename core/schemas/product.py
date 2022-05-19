from decimal import Decimal

from pydantic import BaseModel, constr, condecimal


class ProductBase(BaseModel):
    name: constr(min_length=3, max_length=20)
    description: constr(max_length=200)
    price: condecimal(max_digits=2, decimal_places=2, multiple_of=Decimal('0.25'))


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    class Config:
        orm_mode = True


class ProductUpdate(ProductBase):
    class Config:
        orm_mode = True
