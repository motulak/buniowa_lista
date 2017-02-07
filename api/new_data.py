from pony.orm import *

db = Database()


class User(db.Entity):
    name = Required(str)
    login = Required(str)
    pswd = Required(str)
    items_status = Set('ItemsStatus')

    @db_session
    def display_all_users(self):
        print (User.select().show())

    @db_session
    def add_new_user(self, name, login, pswd):
        if select(p for p in User if p.login == login):
            raise NameError('loginExists')
        else:
            u = User(name=name,login=login,pswd=pswd)
            if select(p for p in User if p.login == login):
                return u


class Category(db.Entity):
    name = Required(str)
    info = Optional(str)
    items = Set('Item')

    @db_session
    def add_category(self, name, info=''):
        if select(c for c in Category if c.name == name):
            raise NameError('categotyNameExists')
        else:
            c = Category(name=name, info=info)
            return c

    @db_session
    def display_all_categories(self):
        print (Category.select().show())



class Item(db.Entity):
    name = Required(str)
    category = Required(Category)
    author = Optional(str)
    items_status = Set('ItemsStatus')

    @db_session
    def display_all_items(self):
        print(Item.select().show())


    @db_session
    def add_new_item(self, name,category, autohr=''):
        if select(i for i in Item if i.name == name):
            raise NameError('itemExists')
        else:
            i = Item(name=name, category=category, author =autohr)
            return i

    @db_session
    def print_single_item_by_id(self,id):
        i = Item[id]
        print(Item.name, Item.category)

    @db_session
    def print_single_item_by_name(self,name):
        i = Item.get(name=name)
        print(i.name, i.category)



class ItemsStatus(db.Entity):
    user = Required(User)
    item = Required(Item)
    have_it = Required(bool)
    packed = Required(bool)

    @db_session
    def add_new_status(self, user, item, have_it=False, packed=False):
        ItemsStatus(user=user, item=item, have_it=have_it, packed=packed)

    @db_session
    def print_statuses_for_user_id(self, user):
        item_s = ItemsStatus.get(user=user)
        print({'login': item_s.user.login, 'item': item_s.item.name, 'have_it': item_s.have_it, 'packed': item_s.packed})



#
#
# class User(db.Entity):
#     name = Required(str)
#     login = Required(str)
#     pswd = Required(str)


#     db.bind('sqlite', 'C:/Temp/db_bunia_list.sqlite', create_db=True)
#     db.generate_mapping(create_tables=True)



class BindAndGenerate():
    db.bind('sqlite', ':memory:')
    # db.bind('sqlite', 'db_bunia_list.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
    sql_debug(False)
#
# class Bind():
#     db.bind('sqlite', 'C:/Temp/db_bunia_list.sqlite', create_db=False)



if __name__ == "__main__":
    BindAndGenerate()
