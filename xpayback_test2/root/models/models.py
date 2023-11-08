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


class Profile(Base):
    __tablename__ = 'profile'

    profile_id = Column(Integer, primary_key=True, index=True)
    profile_pic = Column(String(255))
    user_id = Column(Integer, ForeignKey(Users.user_id))
    user = relationship("Users", backref="Profile")
