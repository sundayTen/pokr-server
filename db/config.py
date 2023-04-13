import hashlib

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

from env import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE, CRYPTO_SALT

database_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_DATABASE,
)

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    with (SessionLocal()) as db:
        yield db


async def encrypt_data(data: str):
    return hashlib.sha256((data + CRYPTO_SALT).encode()).hexdigest()
