from .database import engine, Base ,SessionLocal
import sqlalchemy.orm as orm
from .schemas import UserCreate
from .models import User, Post

# def create_database():
#     return Base.metadata.create_all(bind=engine)


Base.metadata.create_all(bind=engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user_by_user_email(email:str, db:orm.Session):
    return db.query(User).filter(User.email==email).first()


async def create_user(user:UserCreate,db:orm.Session):
    user_obj=User(email=user.email,password=user.password)
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


# async def get_title(title:str, db:orm.Session):
#     return db.query(Post).filter(Post.title==title).first()


# async def create_post(post:Post,db:orm.Session):
#     user_obj=Post(title=post.title)
#     db.add(user_obj)
#     db.commit()
#     db.refresh(user_obj)
#     return user_obj