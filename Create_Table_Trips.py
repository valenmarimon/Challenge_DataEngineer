#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pyodbc
import socket

servername = socket.gethostname()

#Create connection to local server
try:
    conn = pyodbc.connect('Driver={SQL Server};Server='+servername+'\MSSQLSERVER01;Database=Test;Trusted_Connection=yes;')
    cursor = conn.cursor()
    conn.autocommit = True
except:
    print('Error when connecting to Local Server: ' + str(servername))

#If the table doesn't already exists, create it
try:
    cursor.execute('''
    IF EXISTS 
      (SELECT object_id FROM sys.tables
      WHERE name = 'Trips'
      )
        PRINT 'The table does already exist';
    ELSE 
      CREATE TABLE Trips(
        region nvarchar(100),
        origin_coord nvarchar(100),
        destination_coord nvarchar(100),
        date_time datetime2,
        datasource nvarchar(100)
        ) ;
                   ''')
    
    print('Trips table successfully created')
except:
    print('Error when creating Trips table')


# In[ ]:




