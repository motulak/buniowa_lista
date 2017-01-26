import unittest
from flask import json

lista_buni = [
    { "key" :  1 , "name" : "recznik", "group" : "higiena"},
    { "key" : 2 , "name" : "szczoteczka do zębów", "group" : "higiena"},

]

users = [
    { "id": 1 , "user" : "darek" , "lista": lista_buni}
]

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