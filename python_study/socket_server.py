#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket,time,os,sys,commands
import threading,subprocess,logging
import json

def server_init(host = '127.0.0.1', port = 9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)
    while True:
        connection, address = server.accept()
        print 'Connection by', address
        connection.send('welcome')
        while True:
            data = connection.recv(1024)
            if data == 'server_restart':
                connection.close()
                server.close()
                print 'restart server by', address
                return 1
            if data == 'server_stop':
                connection.close()
                server.close()
                print 'close server by', address
                return 0
            if data == 'exit':
                print 'close connection by', address
                break
            connection.send('your send is %s' % (data))
        connection.close()

def Init_log(server_name, log_name, server_file = '/usr/local/service/'):
    global file_read, file_write, file_name
    file_name = log_name

    #检查指定log是否存在指定目录中
    if server_name:
        server_file = server_file + str(server_name) + '/logs/'
    else:
        server_file = './'

    sentences = 'ls %s | grep %s' %(server_file, log_name)
    (status, output) = commands.getstatusoutput(sentences)
    if status:
        print 'Init log error, can\'t do sentences %s' %(sentences)
        return -1
    if not log_name in output:
        print 'Init log error, can\'t find %s in file %s' %(log_name, server_file)
        return -1
    
    #开启log准备读写
    file_write = open(str(log_name), 'w')
    file_read = open(server_file + log_name, 'r')
    file_read.seek(0, 2)

def read_log(imei, time_limit):
    global file_read, file_write

    #先读入一行，确定起始时间
    file_content = file_read.readline()
    time_start = get_time(file_content)
    flag = True

    #循环读入，读到文件结尾、或读time_limit秒的log
    while (file_content or flag):
        if (get_time(file_content) - time_start > time_limit):
            flag = False
        if str(imei) in file_content:
            file_write.write(file_content)
        file_content = file_read.readline()

    file_read.close()
    file_write.close()

def get_time(st_time):
    st = str(st_time)[str(st_time).index(' ') + 1:str(st_time).index('.')]
    time = st[-2:]
    return int(time)

def push(imei, *s):
    #循环加入指定的参数
    sentences = '../auto_test/test --imei %s ' %(imei)
    for i in s:
        sentences = sentences + str(i) + ' '
    output = subprocess.check_output(sentences, shell=True)
    log_write = open('push.log', 'w')
    log_write.writelines(output)
    log_write.close()
    return output

def assert_log(log):
    global file_name
    #读入本地文件，循环断言log
    log_file = open(file_name,'r')
    log_list = log_file.readlines()
    for log_line in log_list:
        if log in log_line:
            log_file.close()
            return True
    return False


if __name__ == "__main__":
    while server_init():
        time.sleep(5)
        server_init()

