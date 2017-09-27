import re

class read_file(object):
    def __init__(self,file_name):
        self.file_name=file_name
    def chose_action(self):
        if self.file_name=='IPTV_CTC':
            self.check_iptv_ctc()
        elif self.file_name=='IPTV_CNC':
            pass
        elif self.file_name=='GE_VPN':
            pass
        elif self.file_name == 'guangdian':
            pass
        elif self.file_name=='wanghailou':
            pass

    def check_iptv_ctc(self):
        file = open(self.file_name,mode='r')
        link_satus={}
        encoder={}
        for line in file:
            if not line:
                break
            if re.search('^Last 300 seconds input rate',line):
                linken = re.split(' ',line)
                link_satus[linken[3]]=linken[5]
            elif re.search('^Last 300 seconds output rate',line):
                linken = re.split(' ', line)
                link_satus[linken[3]] = linken[5]
            if re.search('^ \(.*\,.*\)',line):
                listen =re.split('[ \(\)]',line)
                if listen[3] in encoder.keys():
                    encoder[listen[2]].append(listen[3])
                else:
                    encoder[listen[2]]=[]
                    encoder[listen[2]].append(listen[3])
                    verable = listen[2]
            if re.search('^     UpTime:',line) and encoder!={}:
                listupa = re.split('[ \n]',line)
                encoder[verable].append(listupa[6])
            elif re.search('^             Protocol: pim-sm, UpTime:',line):
                listupa = re.split('[ \n]', line)
                #print(listupa)
                encoder[verable].append(listupa[16])

        print(encoder)

        print('发向IPTV 电信CTC的组播共：' + str(len(encoder)) +'路')

        file.close()
        result=(link_satus,encoder)
        return result