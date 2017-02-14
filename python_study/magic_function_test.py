#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: magic_function_test.py
#              Author: bailiyang@meizu.com
#              Create: 2017-02-13 05:04:03
#       Last Modified: 2017-02-14 03:10:34
#
#--------------------------------------------------

#超类继承调用test
class A():
    def __init__(self):
        self.flag = True

    def do(self):
        assert(self.flag)

class B(A):
    def __init__(self):
        #使用super可以方便的调用超类中的初始化方法初始化
        super(A, self).__init__()
        self.flag = False

#func = B()
#否则使用do方法会报错
#func.do()

#魔法方法阶乘类
class f():
    def __init__(self, max_lenth = 10):
        self.ans = 1
        self.max_lenth = max_lenth
        self.changed = {}

    def __getitem__(self, key):
        #通过key获取value的魔法方法
        if key > self.max_lenth:
            raise IndexError('key beyond the max_lenth')

        try:
            return self.changed[key]
        except:
            for i in range(key):
                self.ans *= (i + 1)

        return self.ans

    def __setitem__(self, key, value):
        #根据key，set value的魔法方法
        if key > self.max_lenth:
            raise IndexError('key beyond the max_lenth')
        
        self.changed[key] = value

    def __len__(self):
        #返回长度的魔法方法
        return self.max_lenth

    def __def__(self):
        #删除的魔法方法，不实现了
        pass

func = f()
#通过key = 5得到value
print '5的阶乘\n' + str(func[5])

#像真正的dict一样，set一个值，再打印
func[5] = 0
print 'set之后5的阶乘\n' + str(func[5])

#打印长度
print '阶乘类的长度\n' + str(len(func))

