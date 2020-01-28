import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
cur.execute('create table Bill(Order_ID int, Cust_ID int,Item char(50),Ord_Date date,QTY )')
