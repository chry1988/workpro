import paramiko,time,re
import datetime

class login(object):
    def __init__(self,user,passwd,hostname,host,comm):
        self.user=user
        self.passwd=passwd
        self.hostname=hostname
        self.host=host
        self.comm=comm
    def inv_login(self):
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(hostname=self.host,username=self.user, password=self.passwd, look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()

        # check iptv groupcast
        for line in self.comm:
            remote_conn.send(line)
            time.sleep(0.4)

        output = remote_conn.recv(1000000000)
        test = output.decode('ascii')
        output_list = re.split(r'[\r\n]', test)
        #for i in output_list:
        #    print(i)
        # 文件处理
        #file_name = str(datetime.datetime.today().strftime('%Y.%m.%d%H.%M.%S')) + 'core'
        file_name = self.hostname
        files = open(file_name, mode='w+')
        files.write(test)
        files.close()
        '''for i in output_list:
            files.write(i)'''
        remote_conn_pre.close()
    def ssh_login(self):
        #exec_command()
        pass
    def ftp_up_load(self):
        pass
    def ftp_down_load(self):
        pass
    pass