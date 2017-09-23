import paramiko,time,re
import datetime

IDC_core=['192.168.248.65']

ip='192.168.248.65'

username='xuedan'
password=''
comm=['screen-length 30 temporary\n','screen-length 0 temporary\n',
      'dis pim routing-table outgoing-interface include vlanif 500\n',
      'dis pim routing-table outgoing-interface include vlanif 360\n',
      'display  interface GigabitEthernet 1/1/1/23\n',
      'display  interface GigabitEthernet 2/1/1/23\n',
      'display this\n',
      'display cu\n']
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

remote_conn=remote_conn_pre.invoke_shell()


#check iptv groupcast
remote_conn.send(comm[1])
time.sleep(1)
remote_conn.send(comm[2])
time.sleep(1)
remote_conn.send(comm[0])
time.sleep(1)
output = remote_conn.recv(10000000)
test=output.decode('ascii')
output_list=re.split(r'[\r\n]',test)
for i in output_list:
    print(i)
#文件处理
file_name=str(datetime.datetime.today().strftime('%Y.%m.%d%H.%M.%S'))+'core'
files=open(file_name,mode='w+')
files.write(test)
files.close()
'''for i in output_list:
    files.write(i)'''
remote_conn_pre.close()