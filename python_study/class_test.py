#!/usr/bin/env python
#-*- coding:utf-8 -*-
#--------------------------------------------------
#
#            Filename: class_test.py
#              Author: bailiyang@meizu.com
#              Create: 2016-11-25 10:19:51
#       Last Modified: 2016-12-26 16:23:37
#
#--------------------------------------------------

foo = {'a' : 1, 'b' : 2}
print repr(foo)
foo = '1'
print repr(foo)
#多态的鸭子类型，无论何种参数，都可以被repr使用

class hello_class():
    #这个类用了全局的name，那么该类的实例在改写这个全局变量的时候，也会影响到其他实例
    def set(self, st):
        global name
        name = st

    def get(self):
        global name
        return name

    def hello(self):
        global name
        print 'hello world, I\'m ' + name

temp = hello_class()
foo = hello_class()
#先set一个值
foo.set('bly')
#再set其他的值，这时候所有实例中的name都被改变了
temp.set('error')
print 'global name return ' + foo.get()
#获取到的就是后面set的那个了
foo.hello()

class hello_class_0():
    #改用self中的name，就不会出现这种情况了
    def set(self, st):
        self.name = st

    def get(self):
        return self.name

    def hello(self):
        print 'hello world, I\'m ' + self.name

temp = hello_class_0()
foo = hello_class_0()
#这两个实例中的name都是独立的了
temp.set('error')
foo.set('bly')
print 'self name in foo return ' + foo.get()
print 'self name in temp return ' + temp.get()
foo.hello()
temp.hello()

class hello_class_1():
    def __set(self, st):
        #注意，_开头代表私有方法，实际上是可以用_hello_class.__set()这样访问的，但是不推荐
        self.name = st

    def set(self, st):
        #只用用这个非私有方法，才能调用__set这个私有方法
        self.__set(st)

    def get(self):
        return self.name

foo = hello_class_1()
foo.set('bly')
#foo.__set('error') 
#这样调用会报错，找不到这个类，但是似乎在开源三方库中，都是用单下划线_这样调用的，也是一种私有方法
print foo.name

#顺手写的一个去掉dir中私有函数的东西，输出值为可以调用的函数
st = [ str(x) for x in dir(hello_class_1) if not '_' in x ]
print '\n'.join(st)

class hello_class_2(hello_class_1):
    #继承与重写，class_2称为class_1的子类，class_1称为class_2的超类（或父类，原意是:super class）
    def set(self, st):
        #重写了超类中的set函数
        st += 'this is in class_2'
        self.name = st
        #这里有个坑，类的私有函数成员，是不可以被继承的，可以理解为这个私有成员，实际上不在class里，而是在_class里，继承class并不能调用_class里的函数

foo = hello_class_2()
foo.set('bly ')
#这里调用的就是重写后的set
print foo.get()
#输出重写后的name

print hasattr(foo, 'get_')
#一个预定义的函数，返某个实例是否有后面这个方法
