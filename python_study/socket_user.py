#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket,time,os,sys,commands,threading
import logging
from kazoo.client import KazooClient 

logging.basicConfig(level=logging.DEBUG,  
        format='%(asctime)s %(name)s [%(filename)s] [%(funcName)s]:(%(lineno)d) %(message)s',  
        datefmt='[%a %d %b %Y %H:%M:%S]')


def zk_init(zk_node, zk_address = '172.16.200.239:2181,172.16.200.233:2181,172.16.200.234:2181'):
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
    print zk_list
    for st in zk_list:
        if ':' in st:
            server_list += [st.split(':')]
    return server_list

def send_one(host, port, content):
    global log_content
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    st = ''
    server.connect((host, port))
    
    try:
        server.sendall(content)
    except:
        logging.error('send TCP content error')

    while True:
        try:
            st += server.recv(1024)
        except:
            logging.error('recv TCP content error')
        if '\\end' in st:
            break
    
        
def test():
    global log_content
    thread_list = []
    mutex = threading.Lock()
 
    st = zk_init('/nebula/log_asserter/mpush')
    for (host, ip) in st:
        send_one(str(host), int(ip), 'server_stop')

if __name__ == "__main__":
    test()
