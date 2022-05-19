from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from ..main.database import Base


class Category(Base):
    """
    This is a base category Model
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship(
        "Product",
        secondary='product_category_m_to_m',
        back_populates="categories"
        # lazy='noload'
    )

    def __init__(self, name):
        self.name = name
        self.products = []

    def __repr__(self):
        return "<Category(id='%d', name='%s')>" % (self.id, self.name)
