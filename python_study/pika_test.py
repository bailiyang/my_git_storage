#!/usr/bin/python
#-*- coding:utf-8 -*-
#   文件名称：pika_test.py
#   创 建 者：bailiyang
#   创建日期：2018年10月29日

import redis, random
import threading


pool = redis.ConnectionPool(host = "127.0.0.1", port = 9233)
head = str(random.randint(0, 1000)) + "_"

def SetString(size):
    client = redis.StrictRedis(connection_pool = pool)
    now_step = 0
    step = int(size / 100)
    print("start set string")

    for i in range(size):
        if i % step == 0:
            now_step+=1
            print("thread %s %d%%" %(threading.current_thread().name, now_step))

        if client.set(head + str(i), i) == False:
            print("set fail in number %d set" %(i))
            break

if __name__ == "__main__":
    size = int(10E6)
    thread_num = 1
    thread_array = []

    for i in range(thread_num):
        t = threading.Thread(target = SetString, name = "threading_" + str(i), args = (int(size / thread_num), ))
        threading.Thread
        t.start()
        thread_array.append(t)

    for t in thread_array:
        t.join()

