#!/usr/bin/env python
#-*- coding:utf-8 -*-
#--------------------------------------------------
#
#            Filename: def_test.py
#              Author: bailiyang@meizu.com
#              Create: 2016-11-24 17:42:26
#       Last Modified: 2016-11-25 09:45:41
#
#--------------------------------------------------

def inc_1(*n):
    #可变参数获取到的是元祖
    print n[0]

foo = [1, 2]
inc_1(foo)
foo = { 1 : 1, 2 : 2}
inc_1(foo)
foo = (1, 2)
inc_1(foo)

def inc_2(**n):
    #这种方式是同时获取关键字跟实参, 输出是一个字典，所以一定要有key（关键字）
    print n

inc_2(x = 1, y = 2, c = 3)

def add(*list):
    res = 0
    for i in list:
        res = res + i
    return res

foo = (1, 2, 3, 4, 5, 6)
#可以这么逆向的使用，这时候传入的就是foo这个参数本身，不再包一层元祖了
print add(*foo)

print [x * x for x in range(10) if x % 2 == 0]
#加了条件的列表推导式，刚好这里用来生成列表

#推导式版本的1到100的加法（显然直接用range更简单）
foo = [x for x in range(100)]
print add(*foo)

#这个版本最简单，但是想要比如纯偶数相加，就不可以了
foo = range(100)
print add(*foo)

def add_1(x, y):
    return x + y

#逆向传参还能这么玩，函数解析出来就是x跟y
print add_1(*[1, 2])

#还可以用**，不过懒得写demo了

#闭包的应用，可以理解为“函数”版本的类
#用了conf决定返回的函数的参数，然后用包含新参数的函数，调用这个函数
#可用于代码复用等
def line_conf(a, b):
    #定义一条直线
    def line(x):
        #为直线求值
        return a * x + b
    return line

foo = line_conf(2, 1)
print 'line = ' + str(foo(2))
