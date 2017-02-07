#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from data_logic import OldList, User, Item, ItemsList
from new_data import *

class TestClassUser(unittest.TestCase):

    def test_check(self):
        BindAndGenerate()
        return True

    def test_add_new_user(self):
        User.display_all_users(self)
        User.add_new_user(self,'TestName','TestLogin','TestPassword')
        User.display_all_users(self)

class TestClassCategory(unittest.TestCase):

    def test_category_add_new_category(self):
        Category.display_all_categories(self)
        Category.add_category(self,'TestCategory','Some info about cateogry')
        Category.display_all_categories(self)


class TestClassItem(unittest.TestCase):

    def test_1_display_all_items(self):
        Item.display_all_items(self)

    def test_2_add_new_Item(self):
        Category.add_category(self, 'Xcat', 'Some info about cateogry')
        Item.add_new_item(self,name='Item1',category=1, autohr='XAuthor')
        self.assertEqual(Item.print_single_item_by_id(self,1), Item.print_single_item_by_name(self,'Item1'))


class TestCalssItemStatus(unittest.TestCase):

    def test_1_add_new_status_item(self):

        User.add_new_user(self, 'UserA', 'UserA', 'Test_UserPassword')
        User.add_new_user(self, 'UserB', 'UserB', 'Test_UserPassword')
        x=User.add_new_user(self, 'UserX', 'UserX', 'Test_UserPassword')
        User.display_all_users(self)
        Category.add_category(self, name='Test_Category')
        Item.add_new_item(self, name='Test_Item', category=1)
        ItemsStatus.add_new_status(self, user=x.id, item=1)
        self.get_by_id=ItemsStatus.print_statuses_for_user_id(self, user=x.id)






if __name__ == '__main__':
    unittest.main()