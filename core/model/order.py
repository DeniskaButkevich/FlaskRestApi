from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP, Column
from sqlalchemy.orm import relationship
from ..main.database import Base


class Order(Base):
    """
    This is a base order Model
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, unique=True)
    address = Column(String, nullable=False)
    date = Column(TIMESTAMP)
    status = Column(Integer)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="orders")

    products = relationship(
        "Product",
        secondary='product_order_m_to_m',
        back_populates="orders",
        lazy='select'
    )

    def __init__(self, address, products, user):
        self.address = address
        self.products = products
        self.status = 1
        self.date = datetime.now()
        self.user = user

    def __repr__(self):
        return "<Product(name='%s', description='%s')>" % (self.name, self.description)