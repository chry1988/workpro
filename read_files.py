import re
file = open('2017.09.2217.17.56core',mode='r')
encoder={}
for line in file:
    if not line:
        break
    if re.search('^ \(.*\,.*\)',line):
        listen =re.split('[ \(\)]',line)
        if listen[3] in encoder.keys():
            encoder[listen[2]].append(listen[3])
        else:
            encoder[listen[2]]=listen[3]

print(encoder)



file.close()