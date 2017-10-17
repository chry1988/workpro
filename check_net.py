import paramiko,time,re,auto_check,read_files
import tempfile
import datetime
'''http://blog.csdn.net/Temanm/article/details/50607741'''
'定义交换机和对应地址'
CORE_DEVICE={'5F-CORE':'172.20.215.254','IDC2-CORE':'192.168.248.65','IDC1-CORE':'192.168.248.62'}
ip='192.168.248.65'
'定义操作内容'
content={'中国有线网管值班电话':['010-68457939','010-68712607','010-68457916',''],
         '韩春梅':['13910788527','市场部如遇困难可联系'],
         '南京至无锡24小时值班电话':['0510-85876580'],
         '蔡工':['15961882568',''],
         '无锡张慎':['15951506918','无锡当地维护主任']}
AC_mess={'poe':['admin','ruijie','ruijie'],'ac':['admin','admin','admin']}
'''paramiko.ssh_exception.AuthenticationException: Authentication failed.'''
sobey={'CORE':'cntv@XCUT','10-2':'CNTV@xcut'}
'输入的命令'
object_list={
    'IPTV_CNC':{
        'ip':'192.168.248.65',
        'comm':['screen-length 0 temporary\n',
            'display interface GigabitEthernet 1/1/1/23\n',
            'dis pim routing-table outgoing-interface include vlanif 500\n',
            'screen-length 30 temporary\n'],
        'bandwidth':'',
        'contacts':[''],
                },
    'IPTV_CTC':{
        'ip':'192.168.248.65',
        'comm':['screen-length 0 temporary\n',
            'display interface GigabitEthernet 2/1/1/23\n',
            'dis pim routing-table outgoing-interface include vlanif 360\n',
            'screen-length 30 temporary\n'],
        'bandwidth':'',
        'contacts':[''],
               },
    'GE_VPN':{
        'ip':'172.20.215.254',
        'comm':[''],
        'bandwidth':'',
        'contacts':[''],
            },
    'guangdian':{
        'ip':'192.168.248.65',
        'comm':[''],
        'bandwidth':'',
        'contacts':[''],
            },
    'wanghailou':{
        'ip':'192.168.248.65',
        'comm':['screen-length 0 temporary\n',
                'display interface GigabitEthernet 1/1/1/19\n',
                'screen-length 30 temporary\n'],
        'contacts':[''],
            },

    }
username='xuedan'
password='1494146442533a'

''' IPTV-CNC 250m IPTV-CTC 250m WANGHAILOU 155m'''


#for i in output_list:
#    print(i)
#文件处理
#file_name=str(datetime.datetime.today().strftime('%Y.%m.%d%H.%M.%S'))+'core'
#files=open(file_name,mode='w+')
#files.write(test)
#files.close()
'''for i in output_list:
    files.write(i)'''
#remote_conn_pre.close()
#print(object_type['IPTV_CNC']['ip'],object_type['IPTV_CNC']['comm'])
#testa=auto_check.login(user=username, passwd=password, host=object['IPTV_CNC']['ip'], comm=object['IPTV_CNC']['comm'])
#testa.inv_login()
def board():
    if __name__ == '__main__':
        pass

def board_test():
    #处理登陆信息
    action_one=auto_check.login(user=username,passwd=password,
                          hostname='IPTV_CNC',host=object_list['IPTV_CNC']['ip'],comm=object_list['IPTV_CNC']['comm'])
    action_one.inv_login()
    #处理收集到的信息
    check_action=read_files.read_file('IPTV_CNC').chose_action()

    print('发往IPTV-CNC的专线状态')
    print('端口状态 ：'+str(check_action[0]['state']))
    print('当前端口使用率：'+str(check_action[0]['Outputbandwidth']))
    print('最近300S平均输入流量 :'+ str(check_action[0]['input']))
    print('最近300S平均输出流量 :'+ str(check_action[0]['output']))
    board_cast_count=[]
    for k in check_action[1]:
        board_cast_count[len(board_cast_count):]=check_action[1][k][::3]
        #print(k,check_action[1][k])
    #print(board_cast_count)
    print('发给CNC的组播共 :'+str(len(board_cast_count)) +'路')

board_test()