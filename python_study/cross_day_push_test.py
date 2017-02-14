#!/usr/bin/env python
#-*- coding:utf-8 -*-
#--------------------------------------------------
#
#            Filename: cross_day_push_test.py
#              Author: bailiyang@meizu.com
#              Create: 2017-02-13 05:03:22
#       Last Modified: 2017-02-13 05:03:24
#
#--------------------------------------------------

import time,commands,sys,json,random
import logging
import requests

logging.basicConfig(level=logging.DEBUG,  
        format='%(asctime)s %(name)s [%(filename)s] [%(funcName)s]:(%(lineno)d) %(message)s',  
        datefmt='[%a %d %b %Y %H:%M:%S]')

def push(imei):
    global zk_address
    if not imei:
        logging.error('no imei')
        return -1
    
    sentences = './push_rpc_test -m 2 -o 0 --address %s --imei %s | grep code' % (str(zk_address), str(imei))
    (status, output) = commands.getstatusoutput(sentences)
    print output

def upload_garcia(date):
    global task_id
    file_read = open('./garcia_post_data.txt')
    read_data = file_read.readlines()
    read_data = ''.join(read_data).strip('\n')
    change_data = json.loads(read_data)
    change_data['task_infos'][0]['task_start_timestamp'] = time.strftime('%Y-%m-%d %X', date)
    change_data['task_infos'][0]['task_end_timestamp'] = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    change_data['task_infos'][0]['task_id'] = str(task_id)
    
    post_data = json.dumps(change_data, separators = (',',':'))
    res = requests.post('http://p.meizu.com/push_data_report/platform/task', data = post_data)
    logging.info('Http requests is ' + str(res.text))
    
    recovery_time()
    file_read.close()

def upload_phone():
    global task_id
    file_read = open('./phone_post_data.txt')
    read_data = file_read.readlines()
    read_data = ''.join(read_data).strip('\n')
    change_data = json.loads(read_data)
    change_data['device_id'] = '868201023408268'
    change_data['event_name'] = 'receive_push_event'
    change_data['timestamp'] = str(int(time.time()))
    change_data['task_id'] = str(task_id) 

    post_data = json.dumps(change_data, separators = (',',':'))
    res = requests.post('https://p.meizu.com/push_data_report/mobile', data = post_data, verify = False)
    print res.text
   
def check_task_info():
    global task_id
    post_data = 'ver=1&' + 'task_id=' + str(task_id)
    res = requests.post('http://p.meizu.com/push_counter/task_info', data = post_data)
    print res.text

def change_success(date):
    #file_write = open('/usr/local/service/mpush/logs/success.log', 'a')
    #file_write.seek(0,2)
    data = '[%s][8491][co:188]|NOTICE|'\
        'push_service.cpp:270:(DoOneWithDevice):'\
        'IMEI=%s APP=com.meizu.pushdemo '\
        'SEQ=%s EXT={"ctl":{"pushType":1},'\
        '"statics":{"taskId":"%s","time":"%s"}} '\
        'EXPIRED=30' %(str(date), '868201023408268', '25', '57', time.mktime(time.strptime(str(date), '%Y-%m-%d %H:%M:%S')))
    data = data.replace('\n','')
    #file_write.writelines(data)
    #file_write.close()
    print data

def change_success(date):
    #file_write = open('/usr/local/service/knob/logs/arrived.log', 'a')
    #file_write.seek(0,2)
    data = '[2016-09-18 18:02:09.827417][1808][co:950]|NOTICE|'\
        'knob_service.cpp:281:(DoFin):IMEI=862416030000645 SEQ=128' %(str(date), '868201023408268', '25')
    data = data.replace('\n','')
    #file_write.writelines(data)
    #file_write.close()
    print data

def change_time():
    date = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    #s = s.replace(s[11:], '23:59:59')
    i = int(date[8:10]) + 1
    date = date.replace(date[8:10], str(i))
    return date

if __name__ == "__main__":
    global zk_address, task_id
    task_id = random.randint(1,100)
    #upload_garcia()
    #upload_phone()
    #time.sleep(2)
    change_success(change_time())
    #change_time()
    #time.sleep(1)
    #recovery_time()
