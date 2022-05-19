from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship

from ..main.database import Base


class Product(Base):
    """
    This is a base product Model
    """
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(20), nullable=False)
    description = Column(String(200))
    price = Column(Float, nullable=False)

    categories = relationship(
        "Category",
        secondary='product_category_m_to_m',
        back_populates="products"
    )
    orders = relationship(
        "Order",
        secondary='product_order_m_to_m',
        back_populates="products"
    )

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return "<Product(name='%s', description='%s')>" % (self.name, self.description)


class ProductOrder(Base):
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


class ProductCategory(Base):
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
