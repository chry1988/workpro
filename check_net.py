import paramiko,time,re,loginservice
import datetime
'''http://blog.csdn.net/Temanm/article/details/50607741'''
IDC_core=['192.168.248.65']
CORE_DEVICE={'5F-CORE':'172.20.215.254','IDC2-CORE':'192.168.248.65','IDC1-CORE':'192.168.248.62'}
ip='192.168.248.65'
content={'中国有线网管值班电话':['010-68457939','010-68712607','010-68457916',''],
         '韩春梅':['13910788527','市场部如遇困难可联系'],
         '南京至无锡24小时值班电话':['0510-85876580'],
         '蔡工':['15961882568',''],
         '无锡张慎':['15951506918','无锡当地维护主任']}
content_IPTV_CTC={}
content_IPTV_CNC={}

username='xuedan'
password=''
comm_office=['screen-length 30 temporary\n','screen-length 0 temporary\n',
             'ping 172.18.41.161\n',
             'display interface XGigabitEthernet 0/0/39\n',
             '\n']
comm_idc_f=['screen-length 30 temporary\n','screen-length 0 temporary\n',
            '\n']
''' IPTV-CNC 250m IPTV-CTC 250m WANGHAILOU 155m'''
comm_idc_s=['screen-length 30 temporary\n','screen-length 0 temporary\n',
            'dis pim routing-table outgoing-interface include vlanif 500\n',
            'dis pim routing-table outgoing-interface include vlanif 360\n',
            'display interface GigabitEthernet 1/1/1/23\n',
            'display interface GigabitEthernet 2/1/1/23\n',
            'display interface GigabitEthernet 1/1/1/19\n',
            'display this\n',
            'display cu\n']

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

remote_conn=remote_conn_pre.invoke_shell()


#check iptv groupcast
remote_conn.send(comm[1])
time.sleep(1)
remote_conn.send(comm[3])
time.sleep(1)
remote_conn.send(comm[0])
time.sleep(1)
output = remote_conn.recv(10000000)
test=output.decode('ascii')
output_list=re.split(r'[\r\n]',test)
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

testa=loginservice.login(user=username,passwd=password,host=CORE_DEVICE['IDC2-CORE'],comm=comm)
testa.inv_login()