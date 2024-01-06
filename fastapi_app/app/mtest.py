# fastapi_app/app/main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://bn_suitecrm:bitnami123@mariadb/bitnami_suitecrm"

# metadata = MetaData()

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


try:
    # Attempt to create the database engine
    engine = create_engine(DATABASE_URL)
    print("Database engine created successfully")
except Exception as e:
    print(f"Error creating database engine: {e}")


try:
    # Attempt to create a session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("Database session created successfully")
except Exception as e:
    print(f"Error creating database session: {e}")
    
Base = declarative_base()
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI, Docker, and Traefik")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
g = get_db()


@app.get("/tasks/")
async def create_task():
    return {"message": "Task created successfully"}
# CRUD operations
# @app.post("/items/")
# async def create_item(item: Item, db: Session = Depends(get_db)):
#     db.add(item)
#     db.commit()
#     db.refresh(item)
#     return item

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, db: Session = Depends(get_db)):
#     item = db.query(Item).filter(Item.id == item_id).first()
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item
