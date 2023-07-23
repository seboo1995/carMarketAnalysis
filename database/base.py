from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from postgreSQLHandler import get_connection_string

engine = create_engine(get_connection_string())
Session = sessionmaker(bind=engine)

Base = declarative_base()