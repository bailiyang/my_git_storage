#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys,time,getopt
import urllib, urllib2, hashlib

st = ''
st = st + 'appId=' + sys.argv[1] + 'appKey=' +sys.argv[3] + 'deviceId=' + sys.argv[2] + sys.argv[3]
print st
st_md5 = hashlib.md5(st).hexdigest()
print st_md5

