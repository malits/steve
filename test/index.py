#!/usr/bin/python

import cgitb
import pymysql
import configparser as cp

cgitb.enable()

config = cp.RawConfigParser()
config.read('../steve.config')
password = config['mysql']['password']

print("Content-Type: text/html")
print()

conn = pymysql.connect(
        db='example',
        user='root',
        passwd='sh@5pp1n',
        host='localhost')
c = conn.cursor()

c.execute("INSERT INTO numbers VALUES (1, 'One!')")
c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
conn.commit()

c.execute("SELECT * FROM numbers")
print([(r[0], r[1]) for r in c.fetchall()])
