from sqlalchemy import Column, Integer, ForeignKey

from ..main.database import db


class ProductCategory(db.Model):
    """
    This is association table for category and product
    """
    __tablename__ = 'product_category_m_to_m'

    category_id = Column(
        Integer,
        ForeignKey('categories.id'),
        primary_key=True)

    product_id = Column(
        Integer,
        ForeignKey('products.id'),
        primary_key=True)
