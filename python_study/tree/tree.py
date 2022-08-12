#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: tree.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-08 14:55:36
#       Last Modified: 2017-03-09 10:16:00
#
#--------------------------------------------------
import pprint

class tree_node():
    def __init__(self, data = ''):
        self.Lchild = None
        self.Rchild = None
        self.data = data 

    def __str__(self):
        return self.data

class tree():
    def __init__(self, tree_str):
        self.tree_iter = iter(tree_str)

    def create_tree(self, tree):
        data = next(self.tree_iter) 
        if data == '#': 
            tree = None
        else:
            tree.data = data
            print 'create %s node' %(tree.data)

            tree.Lchild = tree_node()
            print 'set node %s Lchild' %(tree.data)
            self.create_tree(tree.Lchild)

            tree.Rchild = tree_node()
            print 'set node %s Rchild' %(tree.data)
            self.create_tree(tree.Rchild)

    def preorder(self, tree):
        st = None
        if tree is not None:
            if tree.Lchild:
                st = {tree.data : [tree.Lchild.data]}
            if tree.Rchild:
                st = {tree.data : [tree.Lchild.data, tree.Rchild.data]}
            if st:
                pprint.pprint(st)
            self.preorder(tree.Lchild)
            self.preorder(tree.Rchild)

t = tree_node() 
tree = tree('124#0###35###')
tree.create_tree(t)
tree.preorder(t)

