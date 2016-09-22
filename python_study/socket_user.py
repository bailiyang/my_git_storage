#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket,time,os,sys,commands,threading
import logging
from kazoo.client import KazooClient 

logging.basicConfig(level=logging.DEBUG,  
        format='%(asctime)s %(name)s [%(filename)s] [%(funcName)s]:(%(lineno)d) %(message)s',  
        datefmt='[%a %d %b %Y %H:%M:%S]')


def zk_init(zk_node, zk_address = ''):
    #初始化zk
    zk_cli = KazooClient(hosts = zk_address)
    try:
        zk_cli.start()
    except:
        logging.error('zk Init error, can not connect %s' %(str(zk_address)))
        return -1
    
    try:
        zk_list = zk_cli.get_children(zk_node)
    except:
        logging.error('can not find zk_node %s' %(str(zk_node)))
        return -1
    
    server_list = []
    zk_list = str(zk_list).split('\'')
    for st in zk_list:
        if ':' in st:
            server_list += [st.split(':')]
    return server_list

def socket_init(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(20)
    server.connect((host, port))
    return server

def send_one(server, content):
    #发送单条,并等待回执
    global log_content

    try:
        server.send(content)
    except:
        logging.error('send TCP content error')
        return -1

    data = ''
    try_times = 0
    while True:
        try:
            data += server.recv(1024)
            try_times = try_times + 1
        except:
            if try_times > 5:
                logging.error('recv TCP content error')
                server.close()
                return -1
            else:
                time.sleep(0.1)
                continue
            
        if '\\end' in data:
            logging.info('recv %s' %(data))
            break
    return 0

def save_log(content):
    file_write = open(str(log_name), 'a')
    file_write.writelines(str(content))
    file_write.close()
     
def test():
    global log_content,log_name
    thread_list = []
    mutex = threading.Lock()
    log_name = 'README.md'
    
    st = zk_init('/nebula/log_asserter/mpush')
    for (host, port) in st:
        server = socket_init(str(host), int(port))
        if send_one(server,'log_init,/build/study/,' + log_name) == -1:
            break
        if send_one(server,'log_read,' + '1') == -1:
            break
        if send_one(server,'log_send') == -1:
            break
        send_one(server, 'server_stop')
        server.close()


if __name__ == "__main__":
    test()
