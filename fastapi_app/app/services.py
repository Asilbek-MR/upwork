from  database import engine, Base ,SessionLocal
import sqlalchemy.orm as orm
import models , schemas
import passlib.hash as hash
import fastapi
import fastapi.security as security
import datetime as dt
def create_database():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user_by_user_email(email:str, db:orm.Session):
    return db.query(models.User).filter(models.User.email==email).first()


async def create_user(user:schemas.UserCreate,db:orm.Session):
    user_obj=models.User(email=user.email,password=user.password)
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj