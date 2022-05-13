from flask_restx import fields
from sqlalchemy import Integer, String
from sqlalchemy_utils import EmailType

from ..main.database import db


class User(db.Model):
    """
    This is a base user Model
    """
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    fullname = db.Column(String(100), nullable=False)
    username = db.Column(String(20), nullable=False, unique=True)
    password = db.Column(String(50), nullable=False)
    email = db.Column(EmailType(), nullable=False, unique=True)

    def __init__(self, fullname, username, password, email):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User(fullname='%s', username='%s')>" % (self.fullname, self.username)

    """It's for swagger description"""
    resource_fields = {
        'id': fields.Integer(
            description='id',
            example=14,
            title='should be unique',
            required=True

        ),
        'fullname': fields.String(
            description='Name of person',
            example='Denis Denisov'
        ),
        'username': fields.String(
            description='Username of person',
            example='dez',
            title='should be unique'
        ),
        'password': fields.String(
            description='secret password',
            example='1234'
        ),
        'email': fields.String(
            description='Email',
            example='dez@dez.com',
            title='should be unique'
        )
    }
