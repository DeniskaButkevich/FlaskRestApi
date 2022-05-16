from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP
from flask_restx import fields, Namespace
from sqlalchemy.orm import relationship
from ..model.product import model as ProductModel
from ..main.database import db


class Order(db.Model):
    """
    This is a base order Model
    """
    __tablename__ = 'orders'

    id = db.Column(Integer, primary_key=True, unique=True)
    address = db.Column(String, nullable=False)
    date = db.Column(TIMESTAMP)
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
        self.date = datetime.now()
        self.user = user

    def __repr__(self):
        return "<Product(name='%s', description='%s')>" % (self.name, self.description)


"""It's for swagger description"""
resource_fields = {
    'address': fields.String(
        description='Address of delivery',
        example='GROVE STREET'
    ),
    'date': fields.DateTime(
        description='Date of order',
        example='For doing something'
    ),
    'status': fields.Integer(
        description='Status of order',
        example=2
    ),
    'products': fields.Nested(ProductModel)
}

nested_user = {
    'id': fields.Integer(
        description='id',
        example=14
    ),
    'fullname': fields.String(
        description='Name of person',
        example='Denis Denisov'
    )
}

fields_patch = {
    'status': fields.Integer(
        description='Status of order',
        example=3
    )
}

namespace = Namespace('order', 'CRUD order endpoints')
namespace_user = namespace.model("nested_category", nested_user)

model = namespace.model("Order", resource_fields)
model['user'] = fields.Nested(namespace_user)
model['id'] = fields.Integer(description='id', example='44')

model_put = namespace.model("Order_put", resource_fields)
model_put['user'] = fields.Nested(namespace_user)

model_patch = namespace.model("Order_patch", fields_patch)
