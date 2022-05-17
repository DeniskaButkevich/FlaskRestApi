from flask_restx import fields
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from ..main.database import db


class Category(db.Model):
    """
    This is a base category Model
    """
    __tablename__ = 'categories'

    id = db.Column(Integer, primary_key=True, unique=True)
    name = db.Column(String, unique=True, nullable=False)

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

    """It's for swagger description"""
    resource_fields = {
        'id': fields.Integer(
            description='id',
            example='101'
        ),
        'name': fields.String(
            description='Name of category',
            example='Food'
        )
    }

    update_fields = {
        'name': fields.String(
            description='Name of category',
            example='Food'
        )
    }
