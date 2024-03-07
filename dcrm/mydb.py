import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'your username',
    passwd = 'your password'
    )

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE CRM")

print("All Done!")