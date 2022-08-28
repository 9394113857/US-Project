# importing required libraries
import mysql.connector

# We can connect to the MySQL server using the connect() method.
dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd =""
)

print(dataBase)

# Disconnecting from the server
dataBase.close()
