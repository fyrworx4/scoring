"""
Name: pollMySQL
Description: Will verify that the mySQL service is running on the specific port by checking if authentication to mySQL service is successful, and database matches hard-coded hash
Parameters: ip - ip address to poll, port - port number to poll, users - list of users to connect with, databaseName - name of database to use, tableName - name of table to use, tableHash - hash of table
"""

import mysql.connector
import hashlib

ip = "10.100.10.200"
username = "jarjarbinks"
pw = "rebel#1"
databaseName = "hologram"
tableName = "quotes"
tableHash = "f0c280f803ffa668866b113f453194e5"

try:
    mydb = mysql.connector.connect(
        host = ip,
        user = username,
        password = pw,
        database = databaseName
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM " + tableName)
    output = []
    for x in mycursor:
        output.append(x)
    output = str(output).encode("utf-8")
    
    if(hashlib.md5(output).hexdigest() == tableHash):
        print("True")
    else:
        print("False")
except:
    print("False")