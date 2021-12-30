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
except:
    print('Error when connecting to Local Server: ' + str(servername))
    


# In[2]:


#Function that will show the weekly averages by Region
def avg_Region(reg_selected):
    ## Execute query to determine the average by week for given Region
        ## First, I sum up all trips by day for the given Region
        ## Then, I get the average for each week of the year
    query = cursor.execute('''
    with Counts as (
        SELECT  cast(date_time as date) as datee, count(1) as cnt
        FROM    Trips
        where region=LOWER(?)
        GROUP BY cast(date_time as date)
    )

    SELECT  datepart(YYYY,datee) as Year,DATENAME(ww, datee) as Week_number, avg(cnt) as Trips_avg_by_week
    FROM    Counts
    GROUP BY datepart(YYYY,datee),DATENAME(ww, datee)
    ''',
    reg_selected) 
    new=pd.DataFrame(query)

    df_avg=pd.DataFrame()
    for index,row in new.iterrows():
        dic={}
        for i in range(0,3):
            if i==0:
                dic['Year']=row[0][i]
            elif i==1:
                dic['Week_number']=row[0][i]
            else: dic['Trips_avg_by_week']=row[0][i]
        df_avg = df_avg.append(pd.DataFrame(dic,index=[index]))

            
    print(df_avg)


# In[3]:


#Function that shows the weekly averages by Bounding Box  
def avg_Coord():
    bound_box=[]
    for i in range(1,5):
                    x=0
                    y=0
                    x=float(input('Input X coordinate for point ' + str(i)+ ':'))
                    y=float(input('Input Y coordinate for point ' + str(i)+ ':'))
                    xy_coord=(x,y)
                    bound_box.append(xy_coord)
    #Show the 4 coordinates of the Bounding Box
    # print (bound_box)
    
    #Determine minimum and maximum values for each coordinate of the Bounding Box
    minx=bound_box[0][0]
    maxx=bound_box[0][0]
    maxy=bound_box[0][1]
    miny=bound_box[0][1]
    for seq in bound_box:
        if seq[0]<minx: minx=seq[0]
        if seq[0]>maxx: maxx=seq[0]
        if seq[1]<miny: miny=seq[1]
        if seq[1]>maxy: maxy=seq[1]
    print('Minimum value for X coordinate: ' , str(minx))
    print('Maximum value for X coordinate: ' , str(maxx))
    print('Maximum value for Y coordinate: ' , str(maxy))
    print('Minimun value for Y coordinate: ',str(miny))
    
    # Given a point, if the origin coordinates are within minimum and maximum values determined in the previous step,
    # the trip should be considered in the average
    # I query all the trips that have an origin within the Bounding Box and get the weekly average
    query = cursor.execute('''
    with t2 as (

        Select * from (

            SELECT 
            LEFT(FORMATTED,CHARINDEX(' ', FORMATTED)-1) as first_coord,
            SUBSTRING(FORMATTED,CHARINDEX(' ', FORMATTED)+1,LEN(FORMATTED)) as second_coord,
            Cast(date_time as date) as date_form
            FROM (
            select 
            SUBSTRING(LEFT(origin_coord,LEN(origin_coord)-1),CHARINDEX('(',LEFT(origin_coord,LEN(origin_coord)-1))+1,LEN(LEFT(origin_coord,LEN(origin_coord)-1))) FORMATTED,
            date_time
            FROM TRIPS ) t1
            ) as te
            WHERE  cast(? as float) <  cast(first_coord as float) 
            and cast(first_coord as float) < cast(? as float)
            and cast(? as float) < cast(second_coord as float)
            and cast(second_coord as float) < cast(? as float)
        )


        SELECT  datepart(YYYY,date_form) as Year,
        DATENAME(ww, date_form) as Week_number, 
        avg(cnt) as Trips_avg_by_week
        FROM (
            SELECT date_form, count(1) as cnt
            FROM    t2
            GROUP BY date_form) as test
        GROUP BY datepart(YYYY,date_form),DATENAME(ww, date_form)
     ''',
        minx,
        maxx,
        miny,
        maxy
        ) 
    new=pd.DataFrame(query)

    df_avg=pd.DataFrame()
    for index,row in new.iterrows():
        dic={}
        for i in range(0,3):
            if i==0:
                dic['Year']=row[0][i]
            elif i==1:
                dic['Week_number']=row[0][i]
            else: dic['Trips_avg_by_week']=row[0][i]
        df_avg = df_avg.append(pd.DataFrame(dic,index=[index]))

            
    print(df_avg)
    


# In[5]:



# Develop a way to obtain the weekly average number of trips for an area, defined by a
# bounding box (given by coordinates) or by a region.

try:  
    while True:
        opt = int(input('Obtain weekly average number of trips by coordinates(1) or by region(2) or escape(3): '))
        if opt==1:
            avg_Coord()    
            break
        elif opt==2:
            reg_selected = str(input('Region you want to select:')).lower()
            avg_Region(reg_selected)
            break
        elif opt==3:
            print('Exited menu')
            break
        else: 
            print('Not a valid number')
            continue
        
except: print('Not a number')


# In[ ]:




