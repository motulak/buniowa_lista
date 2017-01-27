#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from data_logic import OldList, User, Item, ItemsList
from createdb import *

class TestClassNewUser(unittest.TestCase):

    def test_check(self):
        return True

    def test_creating_db(self):
        start()
        Customer.show_info(self)




# class TestClassItem(unittest.TestCase):
#
#     def test_Item_Create_new_item(self):
#         item1 = Item('a','b')
#         self.assertEqual(item1.id, 1)
#         self.assertEqual(item1.name,'a')
#         self.assertEqual(item1.category, 'b')
#         self.assertEqual(item1.ammount, 1)
#         self.assertEqual(item1.have_it, False)
#         self.assertEqual(item1.packed, False)
#
#     def test_item_ids(self):
#         item1 = Item('a','b')
#         item2 = Item('c','d')
#         item3 = Item('e', 'f')
#         self.assertEqual(item1.id, 1)
#         self.assertEqual(item2.id, 2)
#
#
#
#
#
#
# class TestClassLista(unittest.TestCase):
#
#     def test_check(self):
#
#         return True
#
#     def test_create_list(self):
#         lista1 = OldList()
#         self.assertEqual(lista1.elements, [])
#
#     def test_intialze(self):
#         lista2 = OldList()
#         lista2.initialize()
#         self.assertEqual(lista2.elements,[ \
#         { "key" :  1 , "name" : "recznik", "group" : "higiena"}, \
#         { "key" : 2 , "name" : "szczoteczka do zębów", "group" : "higiena"}] )
#
#     def test_single_value_return(self):
#         lista1 = OldList()
#         lista1.initialize()
#         self.assertEqual(lista1.return_element(2),{ "key" : 2 , "name" : "szczoteczka do zębów", "group" : "higiena"} )
#         self.assertEqual(lista1.return_element(1), { "key" :  1 , "name" : "recznik", "group" : "higiena"})
#         self.assertEqual(lista1.return_element(0), False)
#
#     def test_add_element_to_a_list(self):
#         lista1 = OldList()
#         lista1.initialize()
#         lista1.add_element('a', 'b')
#         lista1.add_element('c', 'd')
#         self.assertEqual(lista1.return_element(3), {"key": 3, "name": "a", "group": "b"})
#         self.assertEqual(lista1.return_element(4), {"key": 4, "name": "c", "group": "d"})














if __name__ == '__main__':
    unittest.main()