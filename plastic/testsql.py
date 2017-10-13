import mysql.connector
cnx = mysql.connector.connect(user='root',host='127.0.0.1',database='radius', use_pure=False)
query = ("select nasname,shortname from nas")
cursor.execute(query)
for (nasname,shortname) in cursor:
	print ("{},{}").format(nasname,shortname)
cursor.close()
cnx.close()

