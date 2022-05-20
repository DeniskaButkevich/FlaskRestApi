from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session

from core import models
from core.schemas import product as schemas
from core.main.database import get_db

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.get("/{id_product}", response_model=schemas.Product, status_code=status.HTTP_200_OK)
def get_product(id_product: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter_by(id=id_product).first()
    if not product:
        raise HTTPException(status_code=404, detail="Could not find product with that id")

    return product


@router.get("/", response_model=list[schemas.Product], status_code=status.HTTP_200_OK)
def get_all_product(db: Session = Depends(get_db)):
    db_products = db.query(models.Product).all()
    return db_products


@router.post("/", response_model=schemas.Product, status_code=status.HTTP_201_CREATED)
def add_product(product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter_by(name=product.name).first()
    if db_product:
        raise HTTPException(status_code=409, detail="Product name taken...")
    db_product = models.Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    return db_product


@router.put("/{id_product}", response_model=schemas.Product, status_code=status.HTTP_202_ACCEPTED)
def update_product(id_product, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter_by(id=id_product).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product doesn't exist, cannot update")

    if product.name:
        db_product.name = product.name
    if product.description:
        db_product.description = product.description
    if product.price:
        db_product.price = product.price

    db.add(db_product)
    db.commit()
    return db_product


@router.delete("/{id_product}", status_code=status.HTTP_200_OK)
def delete_product(id_product: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter_by(id=id_product).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product doesn't exist, cannot delete")
    db.delete(product)
    db.commit()
    return


@router.post("/all", response_model=list[schemas.Product], status_code=status.HTTP_200_OK)
def add_all_products(products: list[schemas.ProductCreate], db: Session = Depends(get_db)):
    response = []
    for product in products:
        db_product = db.query(models.Product).filter_by(name=product.name).first()
        if db_product:
            continue
        db_product = models.Product(name=product.name, description=product.description, price=product.price)
        response.append(db_product)
        db.add(db_product)
    db.commit()
    return response
