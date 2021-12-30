#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import pyodbc
import socket
servername = socket.gethostname()

#Create connection to local server
try:
    conn = pyodbc.connect('Driver={SQL Server};Server='+servername+';Database=Test;Trusted_Connection=yes;')
    cursor = conn.cursor()
    conn.autocommit = True
except:
    print('Error when connecting to Local Server: ' + str(servername))

#If the database doesn't already exists, create it
try:
    cursor.execute('''IF DB_ID('Test') IS NULL
                      CREATE DATABASE [Test]''')
    print('Database created successfully')
except:
    print('Error when creating the database')


# In[ ]:




