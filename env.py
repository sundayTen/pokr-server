from os import getenv

from dotenv import load_dotenv

load_dotenv(verbose=True)

ENVIRONMENT = getenv("ENVIRONMENT")
DB_USERNAME = getenv("DB_USERNAME")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_DATABASE = getenv("DB_DATABASE")
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = getenv("JWT_ALGORITHM")
ADMIN_USER = getenv("ADMIN_USER")
