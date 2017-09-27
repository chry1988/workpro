import re
file = open('2017.09.2614.43.20core',mode='r')
encoder={}
for line in file:
    if not line:
        break
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