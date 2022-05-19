from fastapi import status, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from core import models
from core import schemas
from core.main.database import get_db

router = APIRouter(
    prefix="/category",
    tags=["Category"],
)


@router.get("/{id_category}/", response_model=schemas.Category, status_code=status.HTTP_200_OK)
def get_category(id_category: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter_by(id=id_category).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Could not find user with that id")
    return category


@router.get("/", response_model=schemas.Category, status_code=status.HTTP_200_OK)
def get_all_category(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@router.post("/", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def add_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    bd_category = db.query(models.Category).filter_by(name=category.name).first()
    if bd_category:
        raise HTTPException(status_code=404, detail="Category name taken...")
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    return db_category


@router.put("/{id_category}/", response_model=schemas.ProductUpdate, status_code=status.HTTP_202_ACCEPTED)
def update_category(id_category: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = models.Category.query.filter_by(id=id_category).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category doesn't exist, cannot update")

    if db_category.name:
        db_category.name = category.name

    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@router.delete("/{id_category}/", status_code=status.HTTP_202_ACCEPTED)
def delete_category(id_category: int, db: Session = Depends(get_db)):
    category = models.Category.query.filter_by(id=id_category).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category doesn't exist, cannot delete")
    db.delete(category)
    db.commit()
    return


@router.patch("/{id_category}/product/{id_product}", response_model=schemas.Category,
              status_code=status.HTTP_202_ACCEPTED)
def add_product_to_category(id_category: int, id_product: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter_by(id=id_category).first()
    product = db.query(models.Product).filter_by(id=id_product).first()
    if not category or not product:
        raise HTTPException(status_code=409, detail="Category or Product not found...")
    category.products.append(product)
    db.commit()
    return category


@router.patch("/{id_category}/product/{id_product}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_to_category(id_category: int, id_product: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter_by(id=id_category).first()
    product = db.query(models.Product).filter_by(id=id_product).first()
    if category or product:
        raise HTTPException(status_code=409, detail="Category or Product not found...")
    category.products.remove(product)
    db.commit()
    return
