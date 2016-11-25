#!/usr/bin/python
#-*- coding:utf-8 -*-
#--------------------------------------------------
#
#            Filename: push_test.py
#              Author: bailiyang@meizu.com
#              Create: 2016-11-24 17:42:17
#       Last Modified: 2016-11-24 17:42:19
#
#--------------------------------------------------

import sys,time,getopt
import urllib, urllib2, hashlib

#url
url = 'https://p.meizu.com/api/push'

#appname test filename
file_name = 'pushkey.txt'

#global data
appname = 'com.meizu.cloud'
content = ''
nonce = str(time.time())
ts = str(time.time())
isDiscard = 'false'
clickType = 1
pushType = 0 
taskid = 1
extra = '{}'
collapse = 0
looptime = 1
ext = ''
expired = 0

#other data
imei = ''
pushkey = ''
md5 = hashlib

#error data
def error():
    print '有参数为空，请检查输入是否正确'

#help data
def help():
    print '支持的格式：'
    print '-a --auto {imei}             全部使用默认值推送一条透传消息，只需要IMEI参数'
    print '-i --imei {imei}             非auto模式必填参数，推送的IMEI，支持IMEI_SN'
    print '-n --appname {appname}       非auto模式必填参数，推送的包名'
    print '-c --content {content}       非必填，推送的内容，默认为一串json格式字符串'
    print '-d --isdiscard {isdiscard}   非必填，是否忽略该消息，默认为false'
    print '-t --clicktype {clicktype}   非必填，点击通知栏效果，默认为1，1-启动应用主界面，2-启动应用任意界面，3-启动web界面'
    print '-p --pushtype {pushtype}     非必填，消息通知类型，默认为0，0-通知栏消息，1-透传消息'
    print '-k --taskid {taskid}         非必填，消息的taskid信息，默认为1'
    print '-e --extra {extra}           非必填，消息的括展字段，默认为空，json格式字符串，以key-value方式显示'
    print '-l --collapse {collapse}     非必填，消息的折叠号，相同collapse的离线消息会被覆盖'
    print '--ext                        非必填，指定ext字段的值（有时应为非空）'
    print '--loop {looptime}            非必填，循环推送的次数，默认为1次'
    print '--dev                        非必填，使用该参数时，会指定在开发环境推送这条消息'
    print '--test                       非必填，使用该参数时，会指定在测试环境推送这条消息'
    print '                             如果不指定推送环境，默认为使用p.meizu.com推送'

#appname to pushkey
def find_app_name():
    global appname,file_name
    try:
        fl = open(file_name)
    except:
        print '找不到名为%s的文件' % file_name
        exit(0)
    file_contant = fl.read()
    if appname in file_contant:
        flag = file_contant.find(appname)
        start = flag + len(appname)
        return str(file_contant[start + 1: start + 7])
    else:
        print '找不到pushkey'
        print '你可以自行加入到pushkey.txt中'
        print '格式为{appname} {pushkey}'
        return ''

#make push
def push():
    global url,appname,token,file_name,content,isDiscard,clickType,pushType,taskid,collapse,extra,looptime,expired

    data = {
        'app': appname,
        'collapse':collapse,
        'content':'{"data":{"content":"test","title":"test","isDiscard": "%s","clickType":"%s","extra":"%s"}}' % (isDiscard, clickType, extra),
        'token': token,
        'nonce': nonce,
        'ts': ts,
        'ext':' ',
        'expired': expired
        }
    if content:
        data['content'] = content
    if pushType and taskid:
        data['ext'] = '{"ctl":{"pushType":"%s"},"statics":{"taskId":"%s"}}' % (pushType, taskid)


    sign_str = 'app=' + data['app'] + '&collapse=' + str(data['collapse']) + '&content=' + data['content']
    sign_str += '&key=' + '80355073480594a99470dcacccd8cf2c'
    sign_str += '&nonce=' + data['nonce'] + '&token=' + data['token'] + '&ts=' + data['ts']

    data['sign'] = md5.md5(sign_str).hexdigest()
    
    sign_str += '&ext=' + data['ext']

#    for o in data:
#        print str(o) + ':' + str(data[o])
#    print ''

    for i in range(looptime):
        #print 'loop %s' % (i)
        try:
            urlenc = urllib.urlencode(data)
            response = urllib2.urlopen(url, urlenc)
            s = response.read()
            if not s:
                logerror('return null string.')
                time.sleep(1)
	    print s
            collapse = collapse + 1
        except:
#            print 'exception: %s' % traceback.format_exc())
            print 'error'
            time.sleep(1)
#        time.sleep(1)

#get opt from argv
def main(argv):
    global url,appname,token,file_name,content,isDiscard,clickType,pushType,taskid,collapse,extra,looptime,ext
    imei = ''
    pushkey = ''

    try:
        opts, value = getopt.getopt(sys.argv[1:], 'ha:i:c:n:d:t:p:k:e:l:', ['help','auto=','imei=','content=','appname=','isdiscard=', 'clicktype=', 'pushtype=', 'taskid=','extra=','collapse=','loop=','test','dev','ext=', 'expired='])
    except:
        error()
        exit(0)

    for o, a in opts:
        if o in ('-h','--help'):
            help()
            exit(0)

        if o in ('-a','--auto'):
            appname = 'com.meizu.cloud'
            pushkey = 100004
            content = '{"flyme_broadcast":{"title":"test","content":"test","url":""}}'
            pushType = 1
            if a:
                imei = str(a)
            else:
                print 'imei非法'
                exit(0)
        
        if o in ('-i','--imei'):
            if a:
                imei = str(a)
            else:
                print 'imei非法'
                exit(0)

        if o in ('-c','--content'):
            if a:
                content = str(a)
            else:
                print 'content非法'
                exit(0)

        if o in ('-n','--appname'):
            if a:
                appname = str(a)
            else:
                print 'appname非法'
                exit(0)
            pushkey = str(find_app_name())
            if pushkey == '':
                exit(0)
            else:
                pushkey = str(pushkey)

        if o in ('-d','--isdiscard'):
            if a:
                isDiscard = str(a)
            else:
                print 'isDiscard非法'
                exit(0)

        if o in ('-t','--clicktype'):
            if a:
                clickType = str(a)
            else:
                print 'clicktype非法'
                exit(0)

        if o in ('-p','--pushtype'):
            if a:
                pushType = str(a)
            else:
                print 'pushtype非法'
                exit(0)

        if o in ('-k','--taskid'):
            if a:
                taskid = str(a)
            else:
                print 'taskid非法'
                exit(0)

        if o in ('-e','--extra '):
            if a:
                extra = str(a)
            else:
                print 'extra非法'
                exit(0)

        if o in ('-l','--collapse'):
            if a:
                try:
                    collapse = int(a)
                except:
                    print 'collapse只能为数字'
                    exit(0)
            else:
                print 'collapse非法'
                exit(0)
        if o in ('--ext'):
            if a:
                ext = str(a)
            else:
                print 'ext非法'
                exit(0)
        if o in ('--expired'):
            if a:
                expired = int(a)
            else:
                print 'expired非法'
                exit(0)

        if o == '--dev':
            url = 'https://172.16.10.96/api/push'

        if o == '--test':
            url = 'https://172.17.49.37/api/push'

        if o == '--loop':
            try:
                looptime = int(a)
            except:
                print 'looptime只能为数字'
                exit(0)


    if not imei:
        print '找不到{imei}'
        print '请输入-i {imei}'
        exit(0)
    elif not pushkey:
        print '找不到{pushkey}'
        print '请输入-a {appname}'
        exit(0)
    else:
        token = str(imei) + str(pushkey)
    #print url
    push()
            
if __name__ == '__main__':
    main(sys.argv)


