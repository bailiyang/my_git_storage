#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: double_list.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-13 14:26:37
#       Last Modified: 2017-03-13 18:11:08
#
#--------------------------------------------------

class list_node():
    def __init__(self, data = None):
        self.data = data
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.data)

class double_list():
    def __init__(self):
        self.root = None

    def increase_node(self, node, node_data):
        if self.root is None:
            #如果没节点，直接设置一个根
            self.root = list_node(node_data)
            self.root.head = self.root.tail = self.root
            return

        if node_data == node.data:
            return
        
        if node_data < node.data:
            #如果插入值比当前节点值小，证明需要插入到当前节点的前继
            node.head.tail = list_node(node_data)
            node.head.tail.head = node.head
            node.head.tail.tail = node
            node.head = node.head.tail
            if node == self.root:
                self.root = node.head
        else:
            #否则继续递归当前节点的后继
            if node.tail == self.root:
                node.tail = list_node(node_data)
                node.tail.head = node 
                node.tail.tail = self.root
                self.root.head = node.tail
            else:
                self.increase_node(node.tail, node_data)
    
    def delete_node(self, node_data, node = None):
        if node is None:
            node = self.root

        if node.data == node_data:
            node.head.tail = node.tail
            node.tail.head = node.head
            if node == self.root:
                self.root = node.tail
            print 'delete node %s success' %(node)
            return node 
        else:
            if node_data > node.data and node_data < node.tail.data:
                return False
            else:
                if node_data > node.data:
                    self.delete_node(node_data, node.tail)
                if node_data < node.data:
                    self.delete_node(node_data, node.head)

    def creat_list(self, list_str):
        for data in list_str:
            print 'add node %s' %(data)
            self.increase_node(self.root, data)
            self.show_list_forward()
            self.show_list_backward()

    def show_list_forward(self, node = None):
        if node is None:
            node = self.root
            self.list_str_forword = str(self.root)
        else:
            #print 'node %s , head %s, tail %s' %(node, node.head, node.tail)
            self.list_str_forword += ' --> ' + str(node.data)

        if not node.tail == self.root or node.tail is None:
            self.show_list_forward(node.tail)
        else:
            print 'forward list  ' + self.list_str_forword

    def show_list_backward(self, node = None):
        if node is None:
            node = self.root.head
            self.list_str_backward = str(self.root.head)
        else:
            #print 'node %s , head %s, tail %s' %(node, node.head, node.tail)
            self.list_str_backward += ' --> ' + str(node.data)

        if not node == self.root or node is None:
            self.show_list_backward(node.head)
        else:
            print 'backward list ' + self.list_str_backward

func = double_list()
import random
list_str = []
n = 100
for i in range(n):
    list_str.append(random.randint(1, n))
func.creat_list([5,6,7,1,2,0,9])
func.delete_node(5)
func.show_list_forward()
func.show_list_backward()
func.delete_node(0)
func.show_list_forward()
func.show_list_backward()

