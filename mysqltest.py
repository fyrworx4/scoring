"""
Name: pollMySQL
Description: Will verify that the mySQL service is running on the specific port by checking if authentication to mySQL service is successful, and database matches hard-coded hash
Parameters: ip - ip address to poll, port - port number to poll, users - list of users to connect with, databaseName - name of database to use, tableName - name of table to use, tableHash - hash of table
"""

ip = "10.100.10.200"
username = "jarjarbinks"
password = "rebel#1"
databaseName = "hologram"
tableName = "quotes"
tableHash = "f0c280f803ffa668866b113f453194e5"

try:
    for user in users:
        if ":" not in user:
            continue
        username = user.split(":")[0]
        password = user.split(":")[1]

    mydb = mysql.connector.connect(
        host = ip,
        user = username,
        password = password,
        database = databaseName
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM " + tableName)
    output = []
    for x in mycursor:
        output.append(x)
    output = str(output).encode("utf-8")
    
    if(hashlib.md5(output).hexdigest() == tableHash):
        return True
        print("True")
    else:
        return False
        print("False")
except:
    return False
    print("False)")