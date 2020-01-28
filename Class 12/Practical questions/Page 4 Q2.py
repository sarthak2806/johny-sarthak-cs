import mysql.connector as my
mysql=my.connect(host='localhost',user='root',password='root',database='school')
cur=mysql.cursor()
cur.execute('create table Sports(Stud_No int,Class int,Name char(50),Game char(50),Grade char(50))')
stud=[x for x in range(10,16)]
clas=