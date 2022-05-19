from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

from ..main.database import Base


class User(Base):
    """
    This is a base user Model
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    email = Column(EmailType(), nullable=False, unique=True)
    orders = relationship("Order", back_populates="user")

    def __init__(self, fullname, username, password, email):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User(fullname='%s', username='%s')>" % (self.fullname, self.username)
