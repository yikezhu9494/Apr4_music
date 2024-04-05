# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:46:47 2024

@author: Zhu Yike
"""
import sqlite3
import datetime
conn = sqlite3.connect("log.db")
conn.execute("create table employee (name text, timestamp timestamp)")
conn = conn = sqlite3.connect("log.db")

c = conn.execute("select * from employee")
c.description
c.close
conn.close()
conn = conn = sqlite3.connect("log.db")
c = conn.cursor()

name = "aa"
timestamp = datetime.datetime.now()
c.execute("insert into employee (name,timestamp) values(?,?)", (name, timestamp))
conn.commit()
c.close()
conn.close()

conn = conn = sqlite3.connect("log.db")
c = conn.execute("select * from employee")
row = ""
for row in c:
    print(row)

c.close()
conn.close()