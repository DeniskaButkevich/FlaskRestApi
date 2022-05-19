from pydantic import BaseModel, constr


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
