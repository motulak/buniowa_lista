from datetime import datetime
from decimal import Decimal
from pony.orm import *


db = Database()


class Customer(db.Entity):
    email = Required(unicode, unique=True)
    password = Required(unicode)
    name = Required(unicode)
    country = Required(unicode)
    address = Required(unicode)
    cart_items = Set('CartItem')
    orders = Set('Order')

    @db_session
    def show_info(self):
        print (show(Customer))



class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(unicode)
    categories = Set('Category')
    description = Optional(unicode)
    picture = Optional(buffer)
    price = Required(Decimal)
    quantity = Required(int)
    cart_items = Set('CartItem')
    order_items = Set('OrderItem')


class CartItem(db.Entity):
    quantity = Required(int)
    customer = Required(Customer)
    product = Required(Product)


class OrderItem(db.Entity):
    quantity = Required(int)
    price = Required(Decimal)
    order = Required('Order')
    product = Required(Product)
    PrimaryKey(order, product)


class Order(db.Entity):
    id = PrimaryKey(int, auto=True)
    state = Required(unicode)
    date_created = Required(datetime)
    date_shipped = Optional(datetime)
    date_delivered = Optional(datetime)
    total_price = Required(Decimal)
    customer = Required(Customer)
    items = Set(OrderItem)


class Category(db.Entity):
    name = Required(unicode)
    products = Set(Product)


def start():
    db.bind("sqlite", "data.sqlite", create_db=True)
    db.generate_mapping(create_tables=True)