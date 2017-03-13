#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: red_black_tree.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-09 14:34:08
#       Last Modified: 2017-03-10 18:03:00
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

    def get_uncle(self):
        if self.father:
            if self.father.father:
                if self.father.father.Lchild == self.father:
                    return self.father.father.Rchild
                if self.father.father.Rchild == self.father:
                    return self.father.father.Lchild
        return None

    def __str__(self):
        return str(self.data)

class red_black_tree():
    def __init__(self):
        self.tree = None
        self.tree_str = []
        self.deep = 0
    
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
            print 'tree root'
            #如果是根节点，置为黑色
            node.colour = tree_node.BLACK
            return

        if self.is_black(node.father) == True:
            print 'father is BLACK'
            #如果父节点为黑色，则为正常
            return

        if self.is_black(node.father) == False and self.is_black(node.get_uncle()) == False:
            print 'father and uncle is RED'
            #如果父节点跟叔节点都是红色，则需要递归
            #父、叔节点换为黑色
            node.father.colour = tree_node.BLACK
            node.get_uncle().colour = tree_node.BLACK

            #祖父节点一定是黑色的，置为红色
            node.father.father.colour = tree_node.RED

            #此时祖父节点一定是错误的，递归处理祖父节点
            self.balance_tree(node.father.father)
        
        if self.is_black(node.father) == False and self.is_black(node.get_uncle()) == True:
            print 'father is RED and uncle is BLACK'
            #如果父节点为红色，叔节点为黑色
            if node.father:
                if node.father.Rchild == node:
                    #如果当前节点是右儿子
                    if node.father.father.Lchild == node.father:
                        print '需要右旋的情况'
                        #且父节点偏左，右旋可以将节点挂在叔节点（BLACK）上
                        self.turn_right(node.father)
                        self.balance_tree(node.father)
                    else:
                        #否则改变父节点、祖父节点颜色，递归
                        node.father.colour = tree_node.BLACK
                        node.father.father.colour = tree_node.RED
                        self.balance_tree(node.father.father)
                else:
                    #如果当前节点是的左儿子                    
                    if node.father.father.Rchild == node.father:
                        print '需要左旋的情况'
                        #且父节点偏右，左旋可以将节点“挂”到叔节点(BLACK)上
                        self.turn_left(node.father)
                        self.balance_tree(node.father)
                    else:
                        #否则就改变父节点、祖父节点颜色，并递归祖父节点
                        node.father.colour = tree_node.BLACK
                        node.father.father.colour = tree_node.RED
                        self.balance_tree(node.father.father)

    def is_black(self, node):
        if node is None:
            return True

        if node.colour == tree_node.BLACK:
            return True
        else:
            return False
    
    def turn_left(self, node):
        #父亲的右儿子指向左儿子，左儿子新父亲为节点的父亲
        node.father.Rchild = node.Lchild
        node.Lchild.father = node.father
        node.Lchild = node.father

        #父亲指向祖父
        if node.father.father is None:
            #如果父亲是根节点，新的根节点指向这个节点
            self.tree = node
            node.father.father = node
            node.father = None
            node.colour = tree_node.BLACK
        else:
            #父亲不是根节点，将祖父节点置为当前节点的父亲
            if node.father.father.Lchild == node.father:
                #如果父节点是左节点，指向这个节点
                node.father.father.Lchild = node
            if node.father.father.Rchild == node.father:
                #父节点是右节点
                node.father.father.Rchild = node
            node.father = node.father.father
            
    def turn_right(self, node):
        #父亲的左儿子指向右儿子，右儿子新父亲为节点的父亲
        node.father.Lchild = node.Rchild
        node.Rchild.father = node.father
        node.Rchild = node.father

        #父亲指向祖父
        if node.father.father is None:
            #如果父亲是根节点，新的根节点指向这个节点
            self.tree = node
            node.father.father = node
            node.father = None
            node.colour = tree_node.BLACK
        else:
            #父亲不是根节点，将祖父节点置为当前节点的父亲
            if node.father.father.Lchild == node.father:
                #如果父节点是左节点，指向这个节点
                node.father.father.Lchild = node
            if node.father.father.Rchild == node.father:
                #父节点是右节点
                node.father.father.Rchild = node
            node.father = node.father.father

    def create_tree(self, tree_str):
        for data in tree_str:
            print 'add now node %s' %(data)
            self.insert_node(data, self.tree)
            self.show()

    def show(self, node = None):
        if node is None:
            node = self.tree

        print 'node data : %s, colour is : %s, Lchild : %s, Rchild : %s, father : %s' %(node, node.colour, node.Lchild, node.Rchild, node.father)
        if node.colour == tree_node.RED:
            assert(self.is_black(node.Lchild))
            assert(self.is_black(node.Rchild))
        if node.Lchild:
            self.show(node.Lchild)
        if node.Rchild:
            self.show(node.Rchild)

    def get_deep(self, level = 0, node = None):
        if node is None:
            node = self.tree

        self.deep = max(self.deep, level)
        
        if node.Lchild:
            self.get_deep(level + 1, node.Lchild)
        if node.Rchild:
            self.get_deep(level + 1, node.Rchild)

    def print_tree(self, level = 0, node = None):
        if node is None:
            self.get_deep()
            for i in range(self.deep + 2):
                self.tree_str.append('')
            print self.deep

            node = self.tree
            self.tree_str[level] += (str(node))
        else:
            print 'level : %s, node %s' %(level, node)
            if node.father.Rchild == node:
                self.tree_str[level] += ' ' * 3 
            self.tree_str[level] += str(node)
            for i in range(level):
                self.tree_str[i] = ' ' + self.tree_str[i]
 
        if node.Lchild:
            self.print_tree(level + 1, node.Lchild)
        else:
            self.tree_str[level + 1] += ' '

        if node.Rchild:
            self.print_tree(level + 1, node.Rchild)
        else:
            self.tree_str[level + 1] += ' ' * 3

func = red_black_tree()
func.create_tree([4,2,1,0,3,5,9,8])
#func.create_tree([2,1,3,5])
func.print_tree()
for i in func.tree_str:
    print i
