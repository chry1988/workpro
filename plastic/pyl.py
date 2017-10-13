def __addline__():
	print "+----+----+"

def __colline__():
	print "|    |    |"

def __printline__ ():
		__addline__() 
		__colline__()
#def print_rueslt():
#input = int(raw_input())
#for i in range(input):
#	__printline__()
def area(radius):
	temp = math.pi * radius**2
	return temp
def add_all(t):
	total = 0
	for x in t:
		total +=x
	return total

