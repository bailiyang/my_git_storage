#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: tree_test.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-06 06:47:49
#       Last Modified: 2017-03-06 07:58:44
#
#--------------------------------------------------
class tree():
    class node():
        def __init__(self, data):
            self.data = data
            self.left_child_node = None
            self.right_child_node = None

        def set_left_child(self, child_data):
            self.left_child_node = node(child_data)

        def set_reght_child(self, child_data):
            self.right_child_node = node(child_data)

        def get_left_child(self):
            return self.left_child_node

        def get_reght_child(self):
            return self.right_child_node

        def __str__(self):
            return self.data

    def __init__(self, tree_str):
        for i, node_data in enumerate(tree_str):
            if i == 0:
                root_node = node(node_data)
                iter_node = root_node
            else:
                if iter_node.left_child_node == None:


    def get_node_data(self, data):
        if data == '*':
            return None  

if __name__ == "__main__":
    node = tree.node('A')
    print node
