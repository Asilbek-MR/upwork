import datetime as dt
from pydantic import BaseModel

class UserBase(BaseModel):
    email:str

class UserCreate(UserBase):
    email:str
    password:str
    class config:
        orm_mode=True

class User(UserBase):
    id :int
    class config:
        orm_mode=True

class LeadBase(BaseModel):
    first_name:str
    last_name:str
    email:str
    company:str
    note:str

class LeadCreate(LeadBase):
    pass
class Lead(LeadBase):
    id :int
    owner_id:int
    created:dt.datetime
    class config:
        orm_mode=True

class Posts(BaseModel):
    title:str
    summary:str