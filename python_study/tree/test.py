#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: test.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-11 00:49:18
#       Last Modified: 2017-03-11 01:31:30
#
#--------------------------------------------------
if __name__ == "__main__":
    import pygraphviz
    g = pygraphviz.AGraph()

    g.node_attr['shape'] = 'circle'
    g.node_attr['color'] = 'red'
    g.node_attr['fontcolor'] = 'white'
    g.node_attr['style'] = 'filled'
    g.add_node(1, label = 'this is node', color = 'black') 


    g.write('./foo.dot')
    g.layout('dot')
    g.draw('./foo.jpg')

    print g

