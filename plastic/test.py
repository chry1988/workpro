import MySQLdb

config = {
	'user':'radius',
	'password':'radiuspass',
	'host':'localhost',
	'database':'radius',
	'raise_on_warnings':True}
cnx = MySQLdb.connect(host="localhost",user="root",passwd="",db="radius")

cursor = cnx.cursor()

cursor.execute("select * from  radacct ")
nas = cursor.fetchall()
for nass in nas:
	print("%s,%s,%s,%s" % (nass[0],nass[1],nass[2],nass[3]))
cursor.close()
cnx.close()
