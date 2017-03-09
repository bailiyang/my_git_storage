#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: red_black_tree.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-09 14:34:08
#       Last Modified: 2017-03-09 09:08:19
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
        self.uncle = None
        self.colour = colour

    def set_uncle(self):
        if self.father:
            if self.father.father:
                if self.father.father.Lchild == self.father:
                    self.uncle = self.father.father.Rchild
                if self.father.father.Rchild == self.father:
                    self.uncle = self.father.father.Lchild

    def __str__(self):
        return str(self.data)

class red_black_tree():
    def __init__(self):
        self.tree = None
        self.step = 1
    
    def insert_node(self, node_data, node):
        if self.tree == None:
            self.tree = tree_node(node_data)
            self.tree.colour = tree_node.BLACK
            return

        if node.data == node_data:
            return

        #如果某个儿子不为空，且符合要求，则set节点
        #构造平衡二叉树
        if node.Lchild == None and node_data < node.data:
            node.Lchild = tree_node(node_data)
            node.Lchild.father = node
            node.Lchild.set_uncle()
            self.balance_tree(node.Lchild)
            return

        if node.Rchild == None and node_data > node.data:
            node.Rchild = tree_node(node_data)
            node.Rchild.father = node
            node.Rchild.set_uncle()
            self.balance_tree(node.Rchild)
            return
        
        if node_data < node.data:
            self.insert_node(node_data, node.Lchild)
        if node_data > node.data:
            self.insert_node(node_data, node.Rchild)

    def balance_tree(self, node):
        print 'balance node %s, father : %s, uncle : %s' %(node, node.father, node.uncle)
        if node == self.tree:
            #如果是根节点，置为黑色
            node.colour = tree_node.BLACK
            return

        if self.is_black(node.father) == True:
            #如果父节点为黑色，则为正常
            return

        if self.is_black(node.father) == False and self.is_black(node.uncle) == False:
            #如果父节点跟叔节点都是红色，则需要递归
            #父、叔节点换为黑色
            node.father.colour = tree_node.BLACK
            node.uncle.colour = tree_node.BLACK

            #祖父节点一定是黑色的，置为红色
            node.father.father.colour = tree_node.RED

            #此时祖父节点一定是错误的，递归处理祖父节点
            self.balance_tree(node.father.father)
        
        if self.is_black(node.father) == False and self.is_black(node.uncle) == True:
            #如果父节点为红色，叔节点为黑色
            if node.father.Rchild == node:
                #如果当前节点是父节点的右儿子, 左旋，并递归原先节点的父节点（旋转后已经是当前节点了）
                if node.father.father.Rchild == node.father:
                    #如果父节点偏右
                    self.turn_left(node)
                if node.father.father.Lchild == node.father:
                    #如果父节点偏左
                    self.turn_right(node)
                self.balance_tree(node)

            if node.father.Lchild == node:
                #如果当前节点是父节点的左儿子，父节点变为黑色，祖父节点变为红色，右旋祖父节点
                node.father.colour = tree_node.BLACK
                node.father.father.colour = tree_node.RED
                if node.father.father.Rchild == node.father:
                    #如果父节点偏右
                    self.turn_left(node.father.father)
                if node.father.father.Lchild == node.father:
                    #如果父节点偏左
                    self.turn_right(node.father.father)
                self.balance_tree(node)

    def is_black(self, node):
        if node is None:
            return True

        if node.colour == tree_node.BLACK:
            return True
        else:
            return False
    
    def turn_left(self, node):
        #如果是跟节点，更换跟节点
        if node == self.tree:
            self.tree = node.Rchild
        else:
            if node.father.Lchild == node:
                node.father.Lchild = node.Rchild
            else:
                node.father.Rchild = node.Rchild

        #否则，先替换原节点为其右儿子
        temp_node = node
        node = node.Rchild

        #将新节点的左儿子，赋给旧节点的右儿子（旧节点的右儿子被替换了）
        temp_node.Rchild = node.Lchild
        #最后，旧节点作为新节点的左儿子
        node.Lchild = temp_node
        node.set_uncle()

    def turn_right(self, node):
        #与左旋一样
        if node == self.tree:
            self.tree = node.Lchild
        else:
            if node.father.Lchild == node:
                node.father.Lchild = node.Lchild
            else:
                node.father.Rchild = node.Lchild

        temp_node = node
        node = node.Lchild

        temp_node.Lchild = node.Rchild
        node.Rchild = temp_node
        node.set_uncle()

    def create_tree(self, tree_str):
        for data in tree_str:
            self.insert_node(data, self.tree)

    def show(self, node = None):
        if node is None:
            node = self.tree

        print 'node data : %s, colour is : %s, Lchild : %s, Rchild : %s' %(node, node.colour, node.Lchild, node.Rchild)
        if node.Lchild:
            self.show(node.Lchild)
        if node.Rchild:
            self.show(node.Rchild)

func = red_black_tree()
func.create_tree([4,2,1,0,3,5,9,8])
print '\n'
func.show()
