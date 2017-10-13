import re
location={}
file=['encoder.txt','stone.txt']
wfile=['enany.txt','stany.txt']
f = open(file[1],mode='r')
afx=0
for line in f:
    if not line:
        break

    testline=re.split('[ \t]',line)
    if len(testline)<4:
        continue
    if testline[1] + ' ' + testline[2] in location.keys():
        pass
    else:
        location[testline[1] + ' ' + testline[2]]=[[],[],[]]
    print(testline)
    location[testline[1] + ' ' + testline[2]][0].append(testline[3])
    location[testline[1] + ' ' + testline[2]][1].append(testline[4])
    if len(testline)>5:
        location[testline[1] + ' ' + testline[2]][2].append(testline[5])

print(len(location))

    #print(testline)
#print(location)
for k in location:
    for i in range(len(location[k])):
        for j in range(len(location[k][i-1])):
            if 'null' in location[k][i-1]:

                location[k][i-1].remove('null')
                #print(location[k][i-1])
    print(k,location[k])
wr=open(wfile[1],mode='w+')
print(len(location))
for k in location:
    note=k+'$'+str(location[k])+'\r\n'
    wr.write(note)
    afx += 1
#print(afx)
wr.close()
f.close()