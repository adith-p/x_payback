import os
from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
MONGO_DATABASE_URI = os.environ.get('MONGO_DATABASE_URI')


client = MongoClient(
    'MONGO_DATABASE_URI')

engine = create_engine(
    'SQLALCHEMY_DATABASE_URI', echo=True)


sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    """
    Return a database session
    """
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


# Config mongo_db client.'database_name'
m_db = client, 'database_name'
