import sqlalchemy as sql
import sqlalchemy.orm as orm
import datetime as dt

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    email = sql.Column(sql.String, unique=True, index=True)
    password = sql.Column(sql.String)
    leads = orm.relationship("Lead", back_populates="owner")
    

class Lead(Base):
    __tablename__ = "leads"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    owner_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    first_name = sql.Column(sql.String, index=True)
    last_name = sql.Column(sql.String, index=True)
    email = sql.Column(sql.String, index=True)
    company = sql.Column(sql.String, index=True, default="")
    note = sql.Column(sql.String, default="")
    date_created = sql.Column(sql.DateTime, default=dt.datetime.utcnow)
    owner = orm.relationship("User", back_populates="leads")


class Post(Base):
    __tablename__ = "post"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    title = sql.Column(sql.String, unique=True, index=True)
    summary = sql.Column(sql.String)