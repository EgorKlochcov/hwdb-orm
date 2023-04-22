import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import *
login = ''
password = ''
name_DB = ''
DSN = f'postgresql://{login}:{password}@localhost:5432/{name_DB}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


param = input("Введите имя издателя: ")

for c in session.query(Book, Shop, Stock, Publisher, Sale).filter(Publisher.id == Book.id_publisher).filter(Book.id == Stock.id_book).filter(Shop.id == Stock.id_shop).filter(Sale.id_stock == Stock.id).filter(Publisher.name == param):
    print(f'{c.Book.title} | {c.Shop.name} | {c.Sale.price} | {c.Sale.date_sale}')

session.close()

