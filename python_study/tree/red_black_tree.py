#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: red_black_tree.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-09 14:34:08
#       Last Modified: 2017-03-09 18:15:48
#
#--------------------------------------------------

class tree_node():
    RED = 'RED'
    BLACK = 'BLACK'
    def __init__(self, data = None, colour = RED):
        self.data = data
        self.Lchild = None
        self.Rchild = None
        self.father = None
        self.colour = colour

    def __str__(self):
        return str(self.data)

class red_black_tree():
    def __init__(self):
        self.tree = None
    
    def insert_node(self, node_data, node):
        if self.tree == None:
            self.tree = tree_node(node_data)
            return
        
        if node.data == node_data:
            return

        #如果某个儿子不为空，且符合要求，则set节点
        if node.Lchild == None and node_data < node.data:
            node.Lchild = tree_node(node_data)
            node.Lchild.father = node
            self.balance_tree(node.Lchild)
            return

        if node.Rchild == None and node_data > node.data:
            node.Rchild = tree_node(node_data)
            node.Rchild.father = node
            self.balance_tree(node.Rchild)
            return
        
        if node_data < node.data:
            self.insert_node(node_data, node.Lchild)
        if node_data > node.data:
            self.insert_node(node_data, node.Rchild)

    def balance_tree(self, node):
        if node == self.tree:
            node.colour = tree_node.BLACK
            return

        if node.father.colour == tree_str.BLACK:
            return

    def turn_left(self, node):
        #如果是跟节点，更换跟节点
        if node == self.tree:
            self.tree = node.Rchild

        #否则，先替换原节点为其右儿子
        temp_node = node
        node = node.Rchild

        #将新节点的左儿子，赋给旧节点的右儿子（旧节点的右儿子被替换了）
        temp_node.Rchild = node.Lchild
        #最后，旧节点作为新节点的左儿子
        node.Lchild = temp_node

    def turn_right(self, node):
        #与左旋一样
        if node == self.tree:
            self.tree = node.Lchild

        temp_node = node
        node = node.Lchild

        temp_node.Lchild = node.Rchild
        node.Rchild = temp_node

    def create_tree(self, tree_str):
        for data in tree_str:
            self.insert_node(data, self.tree)

    def show(self, node = None):
        if node is None:
            node = self.tree

        print 'node data : %s, Lchild : %s, Rchild : %s, father : %s' %(node, node.Lchild, node.Rchild, node.father)
        if node.Lchild:
            self.show(node.Lchild)
        if node.Rchild:
            self.show(node.Rchild)

func = red_black_tree()
func.create_tree([4,2,3,4,5,6,7,1])
func.show()
