#Python Connection to MySQL demo
#Written by: Jeff Brusoe

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="peruser",
  passwd="MyPassword",
  database="per"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM co2;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
