import mysql.connector

con = mysql.connector.connect(user="root", password="root", host="localhost", port="8889", database="dbpython")

cursor=con.cursor()
cursor.execute("INSERT INTO example (id, data)VALUES ('3','AUTO')")

con.commit()
con.close()
