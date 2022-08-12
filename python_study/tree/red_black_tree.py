#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: red_black_tree.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-09 14:34:08
#       Last Modified: 2017-03-13 18:10:54
#       Last Modified: 2017-03-11 05:52:56
#
#--------------------------------------------------
import pygraphviz

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
        self.step = 0
    
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
        #print 'now node is %s Lchild %s Rchild %s uncle %s' %(node, node.Lchild, node.Rchild, node.get_uncle())
        if node == self.tree:
            #print 'tree root'
            #如果是根节点，置为黑色
            node.colour = tree_node.BLACK
            return

        if self.is_black(node.father) == True:
            #print 'node %s father %s is BLACK' %(node, node.father)
            #如果父节点为黑色，则为正常
            return

        if self.is_black(node.father) == False and self.is_black(node.get_uncle()) == False:
            #如果父节点与叔节点为红色
            #print 'node %s father %s and uncle %s is RED' %(node, node.father, node.get_uncle())
            node.father.colour = node.get_uncle().colour = tree_node.BLACK
            node.father.father.colour = tree_node.RED
            self.balance_tree(node.father.father)

        if self.is_black(node.father) == False and self.is_black(node.get_uncle()) == True:
            while True:
                #父节点为红色，叔节点为黑
                if node.father.father.Lchild == node.father and node.father.Lchild == node:
                    #print 'node %s father %s is RED and uncle %s is BLACK, father and grandfather is Lchild' %(node, node.father, node.get_uncle())
                    #如果父节点是左节点，祖父节点也是左节点
                    self.case_1(node)
                    break

                if node.father.father.Rchild == node.father and node.father.Rchild == node:
                    #print 'node %s father %s is RED and uncle %s is BLACK, father and grandfather is Rchild' %(node, node.father, node.get_uncle())
                    #如果父节点是右节点，祖父节点也是右节点
                    self.case_2(node)
                    break

                if node.father.father.Lchild == node.father and node.father.Rchild == node:
                    #print 'node %s father %s is RED and uncle %s is BLACK, father is Rchild and grandfather is Lchild' %(node, node.father, node.get_uncle())
                    #如果祖父节点是左节点，当前节点是右节点
                    self.case_3(node)
                    break

                if node.father.father.Rchild == node.father and node.father.Lchild == node:
                    #print 'node %s father %s is RED and uncle %s is BLACK, father is Lchild and grandfather is Rchild' %(node, node.father, node.get_uncle())
                    #如果祖父节点是右节点，当前节点是左节点
                    self.case_4(node)
                    break

    def case_1(self, node):
        #靠左外侧插入的情况
        self.turn_right(node.father)
        node.father.colour = tree_node.BLACK
        node.father.Rchild.colour = tree_node.RED

    def case_2(self, node):
        #靠右外侧插入的情况
        self.turn_left(node.father)
        node.father.colour = tree_node.BLACK
        node.father.Lchild.colour = tree_node.RED

    def case_3(self, node):
        #父节点是左节点，当前节点是右节点
        self.turn_left(node)
        self.turn_right(node)
        node.colour = tree_node.BLACK
        node.Rchild.colour = tree_node.RED

    def case_4(self, node):
        #父节点是右节点，当前节点是左节点
        self.turn_right(node)
        self.turn_left(node)
        node.colour = tree_node.BLACK
        node.Lchild.colour = tree_node.RED

    def is_black(self, node):
        if node is None:
            return True

        if node.colour == tree_node.BLACK:
            return True
        else:
            return False
    
    def turn_left(self, node):
        #父亲的右儿子指向左儿子，左儿子新父亲为节点的父亲
        #print 'turn left node %s' %(node)
        node.father.Rchild = node.Lchild
        if node.Lchild:
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
            node.Lchild.father = node
            
    def turn_right(self, node):
        #父亲的左儿子指向右儿子，右儿子新父亲为节点的父亲
        #print 'turn right node %s' %(node)
        node.father.Lchild = node.Rchild
        if node.Rchild:
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
            node.Rchild.father = node

    def create_tree(self, tree_str):
        for data in tree_str:
            self.insert_node(data, self.tree)

    def show(self):
        self.print_tree()
        self.printer.write('./foo.dot')
        self.printer.layout('dot')
        self.printer.draw('./foo_%s.jpg' %(self.step))
        self.step += 1

    def print_tree(self, node = None):
        if node is None:
            #初始化绘图
            import pygraphviz
            self.printer = pygraphviz.AGraph(directed = True, strict = False)
            #修改属性
            self.printer.node_attr['shape'] = 'circle'
            self.printer.node_attr['color'] = 'red'
            self.printer.node_attr['fontcolor'] = 'white' 
            self.printer.node_attr['style'] = 'filled'

            #绘制根节点
            node = self.tree
            self.printer.add_node(node.data, color = node.colour)
            
        if node.Lchild or node.Rchild:
            if node.Lchild:
                #如果左儿子存在，绘制一个左儿子节点
                self.printer.add_node(node.Lchild.data, color = node.Lchild.colour)
                #绘制一个边
                self.printer.add_edge(node.data, node.Lchild.data, label = str(node.Lchild.father))
                #递归左儿子
                self.print_tree(node.Lchild)
            else:
                #如果不存在，绘制一个空节点
                self.printer.add_node('Lchild ' + str(node.data), style = 'invis')
                self.printer.add_edge(node.data, 'Lchild ' + str(node.data), style = 'invis')

            if node.Rchild:
                #如果右儿子存在，绘制一个右儿子节点
                self.printer.add_node(node.Rchild.data, color = node.Rchild.colour)
                #绘制一个边
                self.printer.add_edge(node.data, node.Rchild.data, label = str(node.Rchild.father))
                #递归右儿子
                self.print_tree(node.Rchild)
            else:
                #如果不存在，绘制一个空节点
                self.printer.add_node('Rchild ' + str(node.data), style = 'invis')
                self.printer.add_edge(node.data, 'Rchild ' + str(node.data), style = 'invis')
        
    def get_black_deep(self, node = None, deep = 1):
        if node is None:
            node = self.tree
            self.deep = 1

        self.deep = max(self.deep, deep)
        if node.Lchild:
            self.get_black_deep(node.Lchild, deep + 1)
        if node.Rchild:
            self.get_black_deep(node.Rchild, deep + 1)

if __name__ == "__main__":
    import random
    func = red_black_tree()
    tree = []
    n = 1000000
    for i in range(n):
        tree.append(random.randint(1, n))
    func.create_tree(tree)
    #func.create_tree([2,1,3,5])
    func.get_black_deep()
    print 'deep is %s' %(func.deep)
