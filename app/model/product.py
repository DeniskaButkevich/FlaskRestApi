from flask_restx import fields
from sqlalchemy import Integer, String

from ..main.database import db


class Product(db.Model):
    """
    This is a base user Model
    """
    __tablename__ = 'products'

    id = db.Column(Integer, primary_key=True, unique=True)
    name = db.Column(String(20), nullable=False)
    description = db.Column(String(200))
    price = db.Column(Integer, nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return "<User(fullname='%s', username='%s')>" % (self.fullname, self.username)

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
