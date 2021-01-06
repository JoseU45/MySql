import mysql.connector

con = mysql.connector.connect(user="root", password="root", host="localhost", port="8889", database="dbpython")

cursor=con.cursor()
cursor.execute("DELETE FROM `example` WHERE `id`=9;")

con.commit()


cursor.close()
con.close()
