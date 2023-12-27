
from  fastapi import FastAPI
import fastapi 
import sqlalchemy.orm as orm
from .services import get_db, get_user_by_user_email
from .schemas import UserCreate
from .models import User
app=FastAPI()


@app.get('/')
def root():
    return {"Hello":"FastAPI"}

@app.get("/api/users/{email}")
async def get_user(email,db:orm.Session=fastapi.Depends(get_db)):
    return await get_user_by_user_email(email, db)

@app.post('/api/users')
async def create_user(user:UserCreate, db:orm.Session=fastapi.Depends(get_db)):
    db_user=await get_user_by_user_email(user.email,db)
    if db_user:
        raise fastapi.HTTPException(status_code=400,detail="email already in use ")

    return await create_user(user,db)

@app.post('/api/users-create')
async def create_user( user: UserCreate, db:orm.Session=fastapi.Depends(get_db)):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user