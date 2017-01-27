from itertools import count
import unittest
import datetime
from flask import json

lista_buni = [
    {"key": 1, "name": "recznik", "group": "higiena"},
    {"key": 2, "name": "szczoteczka do zębów", "group": "higiena"},

]

users = [
    {"id": 1, "user": "darek", "lista": lista_buni}
]


class Item(object):

    def __init__(self, name, category, ammoun=1):
        self.name = name
        self.category = category
        self.ammount = ammoun
        self.have_it = False
        self.packed = False
        self.update_date = datetime.datetime.now()



class ItemsList(object):
    def __init__(self):
        self.items = []
        self.update_date = datetime.datetime.now()

    def return_elements_in_json(self):
        return json.dumps(self.items)

    def return_element(self,id):
        for item in self.items:
            if id == item.id:
                return item
        else:
            return False

    def add_element(self, name, group):
        self.items.append(Item(name, group))
        self.update_date = datetime.datetime.now()

    def remove_element(self, id):
        for item in self.items:
            if id == item.id:
                self.items.remove(item)


class User(object):
    _num = count(0)

    def __init__(self,name,paswd='pass'):
        self.id = self._num.__next__()
        self.name = name
        self.paswd = paswd
        self.lista = OldList()
        self.items_list = ItemsList()

    def print_user(self):
        print("User {}, | id {} | Password {}".format(self.name, self.id, self.paswd), end=' , ')
        print("{}".format(self.lista.elements))


class OldList(object):
    def __init__(self):
        self.elements = []
        self.update_date = datetime.datetime.now()

    def initialize(self):
        self.elements = list(lista_buni)

    def return_elements(self):
        return json.dumps(self.elements)

    def return_element(self,id):
        for elem in self.elements:
            if id == elem['key']:
                return elem
        else:
            return False

    def add_element(self, name, group):
        index = self.elements.__len__()+1
        new_item = {"key": index, "name":name, "group":group}
        self.elements.append(new_item)
        self.update_date = datetime.datetime.now()

    def remove_element(self,id):
        for elem in self.elements:
            if id == elem['key']:
                self.elements.remove(elem)




if __name__ == '__main__':
    unittest.main()