import mysql.connector
import os


db=mysql.connector.connect(
    host="localhost",
    user="thales",
    passwd=os.getenv("db_psswd"),
    database="main"
)
error=301
cursor=db.cursor()
cursor.execute("select message from ERROR where number = '{}'".format(error))
res = show(cursor)
print(cursor(0))