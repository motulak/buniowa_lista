from itertools import count    
import unittest
from flask import json

lista_buni = [
    { "key" :  1 , "name" : "recznik", "group" : "higiena"},
    { "key" : 2 , "name" : "szczoteczka do zębów", "group" : "higiena"},

]

users = [
    { "id": 1 , "user" : "darek" , "lista": lista_buni}
]


class Element(object):
    _num = count(0)
    def __init__(self, name, category):
        self.key = self._num.__next__()
        self.name
        self.category




class User(object):
    _num = count(0)

    def __init__(self,name,paswd='pass'):
        self.key = self._num.__next__()
        self.name = name
        self.paswd = paswd
        self.lista = Lista()


    def print_user(self):
        print("User {}, | id {} | Password {}".format(self.name, self.key, self.paswd),end=' , ' )
        print("{}".format(self.lista.elements))




class Lista(object):
    def __init__(self):
        self.elements = []

    def initialize(self):
        self.elements = lista_buni

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




if __name__ == '__main__':
    unittest.main()