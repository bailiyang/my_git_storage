#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: magic_function_test.py
#              Author: bailiyang@meizu.com
#              Create: 2017-02-13 05:04:03
#       Last Modified: 2017-03-01 07:00:47
#
#--------------------------------------------------

print '\n' + '-' * 25 + '\n'
print '超类继承调用test'
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

print '\n' + '-' * 25 + '\n'
print '魔法方法阶乘test'
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

print '\n' + '-' * 25 + '\n'
print 'property方法test'
class func():
    def __init__(self, width = 10, hight = 10):
        self.width = width
        self.hight = hight

    def size_get(self):
        return self.width * self.hight

    def size_set(self, size_tuple):
        #这里传参只能传一个，所以用元组的方式
        self.width, self.hight = size_tuple

    def size_clear(self):
        self.__init__()

    size = property(size_get, size_set, size_clear)

f = func()
print '方形的面积是\n' + str(f.size)
f.size = (100, 30)
print '100*30方形的面积是\n' + str(f.size)

print '\n' + '-' * 25 + '\n'
print 'setattr于getattr'
class func():
    def __init__(self, width = 10, hight = 10):
        self.width = width
        self.hight = hight

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.hight = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width * self.hight
        else:
            return self.__dict__[name]
f = func()
print '默认方形的面积是\n' + str(f.size)
f.size = (10, 30)
print '10*30方形的面积是\n' + str(f.size)

print '\n' + '-' * 25 + '\n'
print '阶乘的迭代版本'
class func():
    def __init__(self):
        self.result = 1
        self.result_iter = 0

    def next(self):
        #需要实现next方法（这里好奇怪啊，没有__next__）
        self.result_iter += 1
        self.result *= self.result_iter
        if self.result >= 10e10:
            raise StopIteration
        return self.result_iter, self.result

    def __iter__(self):
        #迭代器魔法方法直接返回实例就行了，在迭代时候自动调用next()这个方法
        return self

f = func()
for i, j in f:
    print '第%d阶阶乘的值为%d' %(i, j)

print '\n' + '-' * 25 + '\n'
print '阶乘的生成器版本'

def func(num):
    result = 1
    for i in num:
        #循环，生成一个阶乘
        result *= i
        #这里不返回result,而是返回迭代器对象，这样可以调用next
        yield result
        
for i, j in enumerate(func([1,2,3,4,5])):
    print '第%d阶阶乘的值为%d' %(i + 1, j)

print '\n' + '-' * 25 + '\n'
print '推导式test'

#这个相当于1到100的和，推导式是能用于（）中的，返回的是可迭代对象
f = sum(i for i in range(100))
print f

print '\n' + '-' * 25 + '\n'
print '推导式八皇后问题'

def is_permit(queen_list, nextX):
    nextY = len(queen_list)
    for i in range(nextY):
        if nextX == queen_list[i] or abs(nextX - queen_list[i]) + abs(nextY - i) == 2:
            #如果X轴上已经有皇后，或者新皇后距离之前皇后距离为根号2（斜线），都算非法
            return False
    #否则合法
    return True

def queens(queen_num = 8, queen_list = ()):
    for i in range(queen_num):
        #一共需要放置8个皇后
        if is_permit(queen_list, i):
            #如果这个皇后是合法的
            if len(queen_list) == queen_num -1:
                #如果是最后一个皇后，直接“返回”这个棋子
                print (i,)
                yield (i,)
            else:
                #如果不是最后一个，证明需要继续查下一个位置
                for j in queens(queen_num, queen_list + (i, )):
                    #每次循环尝试放这个棋子，如果不合适/最后一个，则会返回这个地方重试（通过in后面那个东西实现的）
                    #返回已经放好这个皇后的棋盘
                    print (i,) + j
                    yield (i,) + j

def get_list(queen_list):
    line = '  '
    for i in range(len(queen_list)):
        line += '%d ' %(i + 1)
    print line
    
    for i in range(len(queen_list)):
        line = '%d ' %(i + 1)
        for j in range(len(queen_list)):
            if j == queen_list[i]:
                line += 'X '
            else:
                line += '* '
        print line

import random
get_list(random.choice(list(queens(4))))
