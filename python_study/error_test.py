#!/usr/bin/env python
#-*- coding:utf-8 -*-
#--------------------------------------------------
#
#            Filename: error_test.py
#              Author: bailiyang@meizu.com
#              Create: 2016-11-28 14:53:53
#       Last Modified: 2016-11-28 15:13:59
#
#--------------------------------------------------

#raise Exception('this is error')
#附加错误信息的抛出异常

class SomeErrorInThere(Exception):
    pass
#继承了Exception之后，就能成为自定义的异常

#raise SomeErrorInThere
#试一下抛出

try:
#用try..except捕获异常，也可以直接用元祖方式捕获一堆异常
    x = input('input x: ')
    y = input('input y: ')
    print x / y
except(ZeroDivisionError) as e:
    #as可以捕获异常，但不会终止程序的运行，打印e即为打印异常的内容
    print e
except(NameError):
    print 'your input are not number'
print x / (y + 1)
#这条语句还是会被执行的

