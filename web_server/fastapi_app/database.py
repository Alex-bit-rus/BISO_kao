from databases import Database
from sqlalchemy import create_engine, MetaData
from models import metadata 

DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

metadata.create_all(engine)