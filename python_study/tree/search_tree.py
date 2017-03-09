#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: search_tree.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-09 10:16:27
#       Last Modified: 2017-03-09 15:44:24
#
#--------------------------------------------------

class tree_node():
    def __init__(self, data = ''):
        self.data = data
        self.Lchild = None
        self.Rchild = None

    def __str__(self):
        return str(self.data)

class tree():
    def __init__(self):
        self.tree = None

    def add_node(self, node_data, node):
        if self.tree == None:
            self.tree = tree_node(node_data)
            return
        
        if node.data == node_data:
            return

        if node.Lchild == None and node_data < node.data:
            node.Lchild = tree_node(node_data)
            return

        if node.Rchild == None and node_data > node.data:
            node.Rchild = tree_node(node_data)
            return
        
        if node_data < node.data:
            self.add_node(node_data, node.Lchild)
        if node_data > node.data:
            self.add_node(node_data, node.Rchild)

    def create_tree(self, tree_str):
        for data in tree_str:
            self.add_node(data, self.tree)

    def show(self, node = None):
        if node is None:
            node = self.tree

        print 'node data : %s, Lchild : %s, Rchild : %s' %(node, node.Lchild, node.Rchild)
        if node.Lchild:
            self.show(node.Lchild)
        if node.Rchild:
            self.show(node.Rchild)

    def turn_left(self, node):
        if node == self.tree:
            self.tree = node.Rchild
        temp_node = node
        node = node.Rchild
        temp_node.Rchild = node.Lchild
        node.Lchild = temp_node

func = tree()
func.create_tree([4,2,3,4,5,6,7,1])
func.show()
func.turn_left(func.tree)
print '\n'
func.show()
