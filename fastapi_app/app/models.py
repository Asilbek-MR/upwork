from sqlalchemy import Boolean, Column, String, Integer, ForeignKey,DateTime
import sqlalchemy.orm as orm
import datetime as dt

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    leads = orm.relationship("Lead", back_populates="owner")
    

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    company = Column(String, index=True, default="")
    note = Column(String, default="")
    date_created = Column(DateTime, default=dt.datetime.utcnow)
    owner = orm.relationship("User", back_populates="leads")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    summary = Column(String)