# -*- coding: utf-8 -*-
#2015/6/28建立日志服务器收集核心交换机日志（需要手动查询）
#2015/8/27建立脚本收集日志并发向网络组成员QQ邮箱，增加对二期卫星接收机的检查（ping）
#2015/9/4改为发向网络组成员公司邮箱
#2015/9/15修改了脚本，使得7：00发送的邮件可以查询前一天晚上19：00以后至当天7：00全部的操作命令
#2015/9/18增加办公区二层交换机日志收集（命令统计，4级以上日志汇总）
#2015/9/20添加sobey核心，去掉了二层交换机中4级日志查询改为3级以上日志收集
#2015/10/12去掉接入交换机端口UP/DOWN的消息
#2017.1.1准备将原有csw.sh以python重写，并增加一些新功能
#2017.1.10陈涛建议增加库文件，希望做到即时查询，研究中
#2017.1.10能够根据关键字处理日志，并提供简便的输入方式
#2017.1.13增加处理日志类型函数
import time,datetime,re
    #commands
from collections import Counter
search_key_words = ['report','16:02:04']
source_file = open(r'/home/chry/netmanage/oldshell/log','r',-1)
line_list = 70
#today = time.strftime('%h %d %H:%M:%S')

def printline(line_list=50):
    print('-' * line_list)

def process(line):
    #分割日志文件并返回一个list
    # reline = line.split(' ',)
    reline = re.split('[ ,\(\)]+',line)
    if '\n' in reline:
        reline.remove('\n')
    return reline

def list_test(list1=[],list2=[]):
    #筛选目标list内容
    list_result = False
    for n in list2:
        if n in list1:
            list_result = True
        else:
            list_result = False
            return None
    if list_result == True:
            return list1

def import_message(search=[],default_search=''):
    #读取文本，查找对应内容，如果没有输入内容，则按默认查找条件筛选
        line = source_file.seek(0)
        while True:
            line = source_file.readline()
            if not line:
                break
            line = process(line)
            if search != [] :
                sort_line = list_test(line,search)
                if sort_line != None:
                    yield " ".join(sort_line[3:])
            elif len(line) > 14:
                if line[13] == default_search[0] or line[13] == default_search[1]:
                    yield " ".join(line[17:])

def check_time():
    test_time = int(time.strftime('%d'))
    if  test_time>9:
        today = time.strftime('%h %d')
    elif test_time>1:
        #today = commands.getoutput('date "+%b  %-d"')
        pass
    return today

def re_check_message():
    today = check_time()+'.*command'
    line = source_file.seek(0)
    while True:
        line = source_file.readline()
        if not line:
            break
        if re.search(today,line):
            line = process(line)
            yield " ".join(line[17:])

def message_kind_count():
    #原日志类型统计重写
    count = []
    cnt =Counter()
    line = source_file.seek(0)
    while True:
        line = source_file.readline()
        if not line:
            break
        line = process(line)
        if len(line)>9:
            count.append(line[9])
        for kind in count:
            cnt[kind] += 1
    return cnt

for result_message in import_message(search=[],default_search=['command','Command']):
    print(result_message)

printline()

cnt = dict(message_kind_count())
for key in cnt:
    print(key + ':' + str(cnt[key]))

printline()

net_admin = re_check_message()
for message in net_admin:
    print(message)
source_file.close()