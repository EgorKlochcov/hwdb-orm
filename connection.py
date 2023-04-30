import sqlalchemy
from sqlalchemy.orm import sessionmaker

login = ''
password = ''
name_DB = ''
DSN = f'postgresql://{login}:{password}@localhost:5432/{name_DB}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()