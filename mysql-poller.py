import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor.execute("USE quotes; SELECT * FROM bruh")

for x in mycursor:
  print(x)