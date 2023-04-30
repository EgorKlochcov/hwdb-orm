from sqlalchemy import or_, cast, String
from connection import session, engine
from models import *
from INSERT import insert_data



def get_shops(publisher_params):
    items = session.query(
        Book.title, Shop.name, Sale.price, Sale.date_sale
    ).select_from(Shop)\
        .join(Stock)\
        .join(Book)\
        .join(Publisher)\
        .join(Sale)\
        .filter(or_(cast(Publisher.id, String) == publisher_params, Publisher.name == publisher_params)).all()
    for title, shop, price, date in items:
        print(f"{title: <40} | {shop: <12} | {price: <8} | {date.strftime('%d-%m-%Y')}")


if __name__ == '__main__':
    create_tables(engine)
    insert_data(session)
    param = input("Введите имя издателя или его id: ")
    get_shops(param)

session.close()

