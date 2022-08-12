#!/usr/bin/env python
#-*- coding:utf-8 -*-
__metaclass__ = type
#--------------------------------------------------
#
#            Filename: hash_test.py
#              Author: bailiyang@meizu.com
#              Create: 2017-03-17 11:10:49
#       Last Modified: 2017-03-17 11:44:00
#
#--------------------------------------------------

HASHKEY = 997

class hash_list():
    def __init__(self):
        #初始化hashlist
        self.hash_list = []
        for i in range(HASHKEY):
            self.hash_list.append(0)

    def insert_hash(self, data):
        #计算地址并插入数据
        addr = self.get_hash_key(data)
        if not self.hash_list[addr]:
            #如果有空位，直接插入
            self.hash_list[addr] = data
        else:
            #否则+1或-1后再插入
            flag = 1
            while True:
                if addr + flag > HASHKEY and addr - flag < 0:
                    #实在找不到位置插入，返回失败
                    return False

                if addr + flag <= HASHKEY:
                    if not self.hash_list[self.get_hash_key(addr + flag)]:
                        self.hash_list[self.get_hash_key(addr + flag)] = data
                        break

                if addr - flag >= 0:
                    if not self.hash_list[self.get_hash_key(addr - flag)]:
                        self.hash_list[self.get_hash_key(addr - flag)] = data
                        break

                flag += 1

    def get_hash_key(self, key):
        return key % HASHKEY 

    def search_hash(self, data):
        #用插入方式同样的方式，查找data
        addr = self.get_hash_key(data)
        if self.hash_list[addr] == data:
            return True
        else:
            flag = 1
            while True:
                if addr + flag > HASHKEY and addr - flag < 0:
                    return False

                if self.hash_list[self.get_hash_key(addr + flag)] == data:
                    return True

                if self.hash_list[self.get_hash_key(addr - flag)] == data:
                    return True
                
                flag += 1

if __name__ == "__main__":
    import random
    n = 1000

    hash_list = hash_list()
    for i in range(n):
        data = random.randint(1, n) 
        if hash_list.insert_hash(data) == False:
            print 'insert %s fail' %(data)
        else:
            print 'insert %s success' %(data)
    print hash_list.hash_list
    print hash_list.search_hash(12)
    print hash_list.search_hash(11)
