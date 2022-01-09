#
# CPU Percent Test
#
# Connor Lindsay
#

import psutil
import time
from datetime import datetime
import mysql.connector as connector

# connecting to the database
db = connector.connect(\
    host = 'localhost', \
    user = 'root', \
    password = 'Q]#XlzGv7oFc', \
    database = 'dbtest' )
# Initializing the cursor
cursor = db.cursor()

ID = 2
date = datetime.now().strftime('%Y-%m-%d')
expiramentEntry = 'INSERT INTO expiraments (ExpiramentType, ExpiramentDate) VALUES (%s, %s)'
cursor.execute(expiramentEntry, (ID, date))

expiramentNum = cursor.lastrowid

tableName = 'Data' + str(expiramentNum)
cursor.execute('UPDATE expiraments SET DataID = %s WHERE ID = %s', (tableName, expiramentNum) )

interval = 0.1 # seconds
duration = 10  # seconds
data = []


Tf = time.perf_counter() + duration
Tint = time.perf_counter() + interval
while True:
    t = time.perf_counter() 
    if t > Tint:
        data.append( (str(datetime.now()), psutil.cpu_percent()) )
        Tint += interval
        

    if t > Tf:
        break
    
print(data)

dataTable = 'CREATE TABLE ' + str(tableName) + '
cursor.

db.commit()



