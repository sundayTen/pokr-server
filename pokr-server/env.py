from os import getenv

from dotenv import load_dotenv

load_dotenv(verbose=True)

ENVIRONMENT = getenv("ENVIRONMENT")
DB_USERNAME = getenv("DB_USERNAME")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_DATABASE = getenv("DB_DATABASE")
