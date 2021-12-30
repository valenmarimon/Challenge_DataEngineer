#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import pyodbc
import socket
from send_email import sendMailTo

url = 'trips.csv'
df = pd.read_csv(url)

servername = socket.gethostname()
#Create connection to local server
try:
    conn = pyodbc.connect('Driver={SQL Server};Server='+servername+'\MSSQLSERVER01;Database=Test;Trusted_Connection=yes;')
    cursor = conn.cursor()
except:
    print('Error when connecting to Local Server: ' + str(servername))

# Excecute insert into Table Trips
try:
    for row in df.itertuples():
        cursor.execute('''
                    INSERT INTO Trips (region, origin_coord, destination_coord,date_time,datasource)
                    VALUES (?,?,?,?,?)
                    ''',
                    row.region, 
                    row.origin_coord,
                    row.destination_coord,
                    row.datetime,
                    row.datasource
                    )
    conn.commit()
    
    print('The records were inserted successfully into the SQL database')
      
    sendMailTo()
    print("Email successfully sent")
    
    
except:
    print('Error during the insertion of records')


# In[ ]:




