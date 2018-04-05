import json
import sqlite3
from sqlite3 import Error

#establish connection
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


data1=json.loads(open('port/testing.json').read())

for b in data1:
	
	p1n=b['name']
	d1e=b['description']
	if 'variants' in b:
		v1a=b['variants']  
	p1d=b['portdir']


	c.execute("INSERT INTO port_port (portname,description,variant,portdir) VALUES (?,?,?,?)",(p1n,d1e,v1a,p1d))
	print("completed the INSERT")
	#print(c.fetchall())

conn.commit()
conn.close()

