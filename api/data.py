testfrom pony.orm import *

db = Database()

class Category(db.Entity):
    name = Required(str)
    info = Optional(str)

    @db_session
    def add_category(self, name, info=''):
        Category(name = name, info=info)

    @db_session
    def display_all_categories(self):
        print (Category.select().show())



class Item(db.Entity):
    name = Required(str)
    author = Optional(str)


class ItemsStatus(db.Entity):
    user = Required("User")
    item = Required(Item)
    have_it = Required(bool)
    packed = Required(bool)


class User(db.Entity):
    name = Required(str)
    login = Required(str)
    pswd = Required(str)


class BindAndGenerate():
    db.bind('sqlite', 'C:/Temp/db_bunia_list.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
    sql_debug(True)

class Bind():
    db.bind('sqlite', 'C:/Temp/db_bunia_list.sqlite', create_db=False)



if __name__ == "__main__":
    db = Database()
    sql_debug(True)

