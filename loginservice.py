import paramiko,time,re
import datetime

class login(object):
    def __init__(self,user,passwd,host,comm):
        self.user=user
        self.passwd=passwd
        self.host=host
        self.comm=comm
    def inv_login(self):
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(hostname=self.host,username=self.user, password=self.passwd, look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()

        # check iptv groupcast
        remote_conn.send(self.comm[1])
        time.sleep(1)
        remote_conn.send(self.comm[2])
        time.sleep(1)
        remote_conn.send(self.comm[0])
        time.sleep(1)
        output = remote_conn.recv(10000000)
        test = output.decode('ascii')
        output_list = re.split(r'[\r\n]', test)
        for i in output_list:
            print(i)
        # 文件处理
        file_name = str(datetime.datetime.today().strftime('%Y.%m.%d%H.%M.%S')) + 'core'
        files = open(file_name, mode='w+')
        files.write(test)
        files.close()
        '''for i in output_list:
            files.write(i)'''
        remote_conn_pre.close()
    def ssh_login(self):
        pass

    pass