list_one=[]
list_two=[]
with open('changestatus',mode='r') as read_file,open('changecomm',mode='w') as write_file :
    for line in read_file:
        if not line:
            break
        list_one.append(line)
    for i in range(0,len(list_one)):
        list_two.append(list_one[i])
        list_two.append('shutdown\n')
    for i in range(0,len(list_two)):
        write_file.write(list_two[i])