import mysql.connector
sql=mysql.connector.connect(host="localhost",user="root",password="root")
cur=sql.cursor()
cur.execute('create database game')
cur.execute('drop database game')