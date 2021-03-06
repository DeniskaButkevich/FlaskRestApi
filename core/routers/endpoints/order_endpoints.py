from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session

from core import models
from core.schemas import order as schemas
from core.main.database import get_db

router = APIRouter(
    prefix="/order",
    tags=["Order"]
)


@router.get("/{id_order}/", response_model=schemas.Order, status_code=status.HTTP_200_OK)
def get_order(id_order: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter_by(id=id_order).first()
    if not order:
        raise HTTPException(status_code=404, detail="Could not find order with that id")
    return order


@router.get("/", response_model=list[schemas.Order], status_code=status.HTTP_200_OK)
def get_all_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()


@router.post("/", response_model=schemas.Order, status_code=status.HTTP_201_CREATED)
def post(order: schemas.OrderCreate, db: Session = Depends(get_db)):

    db_products = db.query(models.Product).where(models.Product.id.in_(order.product_ids)).all()

    db_order = models.Order(address=order.address, products=db_products, user_id=order.user_id)
    db.add(db_order)
    db.commit()
    return db_order


@router.put("/{id_order}/", response_model=schemas.Order, status_code=status.HTTP_202_ACCEPTED)
def update_order(order: schemas.OrderUpdate, id_order: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter_by(id=id_order).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order doesn't exist, cannot update")
    if order.status:
        db_order.status = order.status

    db.commit()
    return db_order


@router.delete("/{id_order}/", status_code=status.HTTP_200_OK)
def delete(id_order: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter_by(id=id_order).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order doesn't exist, cannot delete")
    db.delete(order)
    db.commit()
    return
