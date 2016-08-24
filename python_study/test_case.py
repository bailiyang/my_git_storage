#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
sys.path.append("..")
from auto_test import auto_test
import os,logging,random,time

imei = 868201023408268

def push_send_V1(imei):
    rand = random.randint(1, 10000)

    auto_test.Init_log('mpush', 'success.log')
    push_list = ('-o 0', '-m 1', '--ext %s' %(rand))
    
    output = auto_test.push(imei, *push_list)
    if not 'code=200' in output:
        logging.error('send to rpc error')
        return -1
    logging.info('send to rpc OK')

    time.sleep(1)
    auto_test.read_log(imei, 1)
    if auto_test.assert_log('EXT=' %(rand)) == False:
        logging.error('storage push error')
        return -1   
    logging.info('storage push OK')

if __name__ == "__main__":
    push_send_V1(imei)
