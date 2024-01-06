from venv import create
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base as d_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL="sqlite:///./sql_app.db"
DATABASE_URL = "mysql://bn_suitecrm:bitnami123@mariadb/bitnami_suitecrm"
# DATABASE_URL="mysql://bn_suitecrm:bitnami123@mariadb:3306/bitnami_suitecrm"

# DATABASE_URL = "mysql://bn_suitecrm:bitnami123@mariadb:3306/bitnami_suitecrm"

engine= create_engine(DATABASE_URL)

SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = d_base()