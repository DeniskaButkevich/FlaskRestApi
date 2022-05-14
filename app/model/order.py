from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP
from flask_restx import fields
from sqlalchemy.orm import relationship

from ..main.database import db


class Order(db.Model):
    """
    This is a base order Model
    """
    __tablename__ = 'orders'

    id = db.Column(Integer, primary_key=True, unique=True)
    address = db.Column(String, nullable=False)
    data = db.Column(TIMESTAMP)
    status = db.Column(Integer)

    user_id = db.Column(Integer, ForeignKey('users.id'))
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
        self.data = datetime.now()
        self.user = user

    def __repr__(self):
        return "<Product(name='%s', description='%s')>" % (self.name, self.description)

    """It's for swagger description"""
    resource_fields = {
        'id': fields.Integer(
            description='id',
            example='44'
        ),
        'name': fields.String(
            description='Name of product',
            example='Spun'
        ),
        'description': fields.String(
            description='Descriptions of product',
            example='For doing something'
        ),
        'price': fields.Integer(
            description='Price via BigInteger',
            example=33
        )
    }
