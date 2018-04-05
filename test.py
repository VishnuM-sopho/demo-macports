import json
import sqlite3
from sqlite3 import Error

#establish connection
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


k= """{
    "variants"         : "universal",
    "portdir"          : "lang/python247",
    "description"      : "An interpreted coding language",
    "homepage"         : "https://www.python.org/",
    "depends_run"      : "port:python_select",
    "epoch"            : "0",
    "platforms"        : "darwin",
    "name"             : "python24",
    "depends_lib"      : "port:gettext path:lib/libssl.dylib:openssl",
    "license"          : "PSF",
    "long_description" : "Python is an interpreted, interactive, object-oriented programming language.",
    "maintainers"      : "fourdigits.nl:roel openmaintainer",
    "categories"       : "lang",
    "version"          : "2.4.6",
    "revision"         : "12"
}
"""
def jsonparser(json1):
    obj = json.loads(json1)
    return obj

b=jsonparser(k)

p1n=b['name']
d1e=b['description']
v1a=b['variants']
p1d=b['portdir']

c.execute("INSERT INTO port_port (portname,description,variant,portdir) VALUES (?,?,?,?)",(p1n,d1e,v1a,p1d))
print("completed the INSERT")
#print(c.fetchall())

conn.commit()
conn.close()


#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#code to print all tables in database


#code to update the database from json
#c.execute("INSERT INTO port (portname,description,variant,portdir) VALUES ( {pn},{de},{va},{pd} )".format(pn=p1n, de=d1e, va=v1a, pd=p1d))
#str="INSERT INTO port (portname,description,variant,portdir) VALUES ",(p1n,d1e,v1a,p1d)
#print(str)
