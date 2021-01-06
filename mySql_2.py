import mysql.connector

con = mysql.connector.connect(user="root", password="root", host="localhost", port="8889", database="dbpython")

cursor=con.cursor()
cursor.execute("SELECT * FROM `example` WHERE `id`=9")

rows = cursor.fetchall()

for row in rows:
    print(row)
    
cursor.close()
con.close()
