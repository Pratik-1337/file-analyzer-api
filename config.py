from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    DEBUG = os.getenv("DEBUG", "False") == "True"
    DB_NAME = os.getenv("DB_NAME", "report.db")
    DB_PATH = os.path.join(BASE_DIR, DB_NAME)
    APP_ENV = os.getenv("APP_ENV", "development")