#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from data_logic import Lista

class TestClassLista(unittest.TestCase):

    def test_check(self):
        return True

    def test_create_list(self):
        lista1 = Lista()
        self.assertEqual(lista1.elements, [])

    def test_intialze(self):
        lista1 = Lista()
        lista1.initialize()
        self.assertEqual(lista1.elements,[ \
        { "key" :  1 , "name" : "recznik", "group" : "higiena"}, \
        { "key" : 2 , "name" : "szczoteczka do zębów", "group" : "higiena"}] )

    def test_single_value_return(self):
        lista1 = Lista()
        lista1.initialize()
        self.assertEqual(lista1.return_element(2),{ "key" : 2 , "name" : "szczoteczka do zębów", "group" : "higiena"} )
        self.assertEqual(lista1.return_element(1), { "key" :  1 , "name" : "recznik", "group" : "higiena"})
        self.assertEqual(lista1.return_element(0), False)

    def test_add_element_to_a_list(self):
        lista1 = Lista()
        lista1.initialize()
        lista1.add_element('pasta do zębów', 'higiena')
        self.assertEqual(lista1.return_element(3), {"key": 3, "name": "pasta do zębów", "group": "higiena"})






if __name__ == '__main__':
    unittest.main()