from sqlalchemy import Column, Integer, ForeignKey

from ..main.database import db


class ProductOrder(db.Model):
    """
    This is association table for product and order
    """
    __tablename__ = 'product_order_m_to_m'

    product_id = Column(
        Integer,
        ForeignKey('products.id'),
        primary_key=True)

    order_id = Column(
        Integer,
        ForeignKey('orders.id'),
        primary_key=True)
