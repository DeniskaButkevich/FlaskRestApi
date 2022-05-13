from sqlalchemy import Integer, String
from sqlalchemy_utils import EmailType
from flask_restful import fields
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

    resource_fields = {
        'id': fields.Integer,
        'fullname': fields.String,
        'username': fields.String,
        'password': fields.String,
        'email': fields.String
    }

    def __init__(self, id, fullname, username, password, email):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User(fullname='%s', username='%s')>" % (self.fullname, self.username)
