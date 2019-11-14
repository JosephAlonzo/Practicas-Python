import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythontest"
)

mycursor = mydb.cursor()

sql = "INSERT INTO usuario (nombre, apellidos, correo) VALUES (%s, %s, %s)"
val = ("joseph", "alonzo", "josep_alonzo@icloud.com")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM usuario")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)