import sqlalchemy
from sqlalchemy.orm import sessionmaker

login = 'postgres'
password = 'StalKer333'
name_DB = 'home_work5'
DSN = f'postgresql://{login}:{password}@localhost:5432/{name_DB}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()