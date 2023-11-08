import uuid
from sqlalchemy import BINARY, Column, Integer, String, BLOB, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy_utils import EmailType, UUIDType
from database.database import Base


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    fullname = Column(String(255))
    email = Column(EmailType, unique=True)
    password = Column(String)
    phone = Column(String, unique=True)
