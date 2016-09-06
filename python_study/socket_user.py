#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.174.129', 9999))

st = ''
print 'log init'
s.sendall('log_init,decrypt_v2.txt,/build/tool/')
while True:
    st += s.recv(1024)
    if '\\end' in st:
        print st
        break
st = ''

print 'log_read'
s.sendall('log_read,is')
while True:
    st += s.recv(1024)
    if '\\end' in st:
        print st
        break
st = ''

print 'log_send'
s.sendall('log_send')
while True:
    st += s.recv(1024)
    if '\\end' in st:
        print st
        break
s.sendall('server_stop')
