#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket,time,os,sys,commands
import logging,urlparse
from kazoo.client import KazooClient 

logging.basicConfig(level=logging.DEBUG,  
        format='%(asctime)s %(name)s [%(filename)s] [%(funcName)s]:(%(lineno)d) %(message)s',  
        datefmt='[%a %d %b %Y %H:%M:%S]')

def zk_init(server_address, zk_node, zk_address = ''):
    #初始化zk节点
    zk_cli = KazooClient(hosts = zk_address)
    try:
        zk_cli.start()
    except:
        logging.error('zk Init error, can not connect %s' %(str(zk_address)))
        return -1
    
    try:
        zk_cli.get(zk_node)
    except:
        logging.warn('can not find zk path %s, creat it' %(str(zk_node)))
        zk_cli.ensure_path(zk_node)

    if zk_node[-1] != '/':
        zk_node += '/'
        
    try:
        zk_cli.create(zk_node + server_address, '1', ephemeral=True)
    except:
        if zk_cli.get(zk_node + server_address):
            return 0
        else:
            logging.error('create zk_node error, can not create node %s' %(str(zk_node) + str(zk_address)))
            return -1
    return 0

def get_ip_address(ip = '.'):
    #通过ip关键字获取本机ip地址，找不到返回第一个获取到的ip
    (status, output) = commands.getstatusoutput('ifconfig | grep inet | awk \'{print $2}\' | cut -d : -f 2')
    ip_list = str(output).split()
    logging.info('ip list is %s' %(str(ip_list)))
    for st in ip_list:
        if ip in st:
            return st
    return ip_list[0]

def server_init(host = '127.0.0.1', port = 9999):
    #开启TCP服务
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket.setdefaulttimeout(20)

    server.bind((host, port))
    server.listen(1)
    while True:
        #服务启动，循环接收连接
        connection, address = server.accept()
        logging.info("recv connection from %s" %(str(address)))
        while True:
            #连接启动，循环接收连接的信息并处理
            #logging.info('recv')
            data = connection.recv(1024)
            if data == 'server_restart':
                connection.send('%s:%s restart\\end' %(str(host), str(port)))
                connection.close()
                server.close()
                logging.warn("restart server by %s" %(str(address)))
                time.sleep(10)
                return 0

            if data == 'server_stop':
                connection.send('%s:%s stop\\end' %(str(host), str(port)))
                connection.close()
                server.close()
                logging.warn("close server by %s" %(str(address)))
                return -1

            if data == 'exit':
                connection.send('%s:%s exit\\end' %(str(host), str(port)))
                connection.close()
                logging.info("address %s connection close" %(str(address)))
                break

            if 'log_init' in data:
                data_split = str(data).split(',')
                logging.info('start Init log by %s' %(str(address)))
                if Init_log(data_split[2], data_split[1]):
                    connection.send('Init log error\\end')
                    break
                else:
                    connection.send('Init log OK\\end')
                    logging.info('Init log OK')
                continue
                    
            if 'log_read' in data:
                logging.info('start read log')
                data_split = str(data).split(',')
                if len(data_split) > 2:
                    status = read_log(data_split[1],data_split[2])
                else:
                    status = read_log(data_split[1])
                    
                if status:
                    connection.send('read log error\\end')
                else:
                    connection.send('read log OK\\end')
                continue

            if 'log_send' in data:
                logging.info('start send log')
                try:
                    for st in get_send_log():
                        connection.send(st)
                    connection.send('\\end')
                except:
                    logging.error('send log error\\end')
                    connection.send('send log error')
                continue
   
        connection.close()

def Init_log(log_name, server_file = '/usr/local/service/'):
    global file_read, file_write, file_name
    file_name = log_name

    #检查指定log是否存在指定目录中
    sentences = 'ls %s | grep %s' %(server_file, log_name)
    try:
        (status, output) = commands.getstatusoutput(sentences)
    except:
        logging.error('Init log error, can\'t do sentences %s' %(str(sentences)))
        return -1

    if not log_name in output:
        logging.error('Init log error, can\'t find %s in file %s' %(str(log_name), str(server_file)))
        return -1
    
    #开启log准备读写
    file_write = open(str(log_name), 'w')
    file_read = open(server_file + log_name, 'r')
    #file_read.seek(0, 2)
    logging.info('start log assert, file_read=%s' %(server_file + log_name))
    return 0

def read_log(grep_key, time_limit = 5):
    global file_read, file_write

    #先读入一行，确定起始时间
    time_start = get_time()

    #循环读入，读到文件结尾、或读time_limit秒的log
    while True:
        time_now = get_time()
        if (int(time_now) - int(time_start)) > int(time_limit):
            break

        try:
            content = file_read.readline()
        except:
            logging.error('read log error')
            return -1
        if content == '':
            break
        if str(grep_key) in content:
            try:
                file_write.write(content)
            except:
                logging.error('write log error')
                return -1

    logging.info('read&write log OK, file_write=%s' %(file_name))
    file_read.close()
    file_write.close()
    return 0

def get_time():
    #获取当前系统时间戳
    sentences = str('date +%s')
    (status, output) = commands.getstatusoutput(sentences)
    try:
        time = int(output)
    except:
        logging.error('get time from date error, output is %s' %(str(output)))
        return -1
    return time

def get_send_log():
    #获取需要发送的log
    global file_name
    file_write = open(str(file_name), 'r')
    st = file_write.readlines()
    file_write.close()
    return st

if __name__ == "__main__":
    while True:        
        ip = get_ip_address('192')
        if ip == -1:
            break
        if zk_init(str(ip) + ':9999', zk_node = '/nebula/log_asserter/mpush'):
            break
        if server_init(ip):
            break
            time.sleep(1)
