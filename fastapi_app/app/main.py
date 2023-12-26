
from  fastapi import FastAPI
import fastapi 
import sqlalchemy.orm as orm
import services,schemas


app=FastAPI()


@app.get('/')
def root():
    return {"Hello":"FastAPI"}

@app.get("/api/users/{email}")
async def get_user(email,db:orm.Session=fastapi.Depends(services.get_db)):
    return await services.get_user_by_user_email(email, db)

@app.post('/api/users')
async def create_user(user:schemas.UserCreate, db:orm.Session=fastapi.Depends(services.get_db)):
    db_user=await services.get_user_by_user_email(user.email,db)
    if db_user:
        raise fastapi.HTTPException(status_code=400,detail="email already in use ")

    return await services.create_user(user,db)