# -*- coding: utf-8 -*-
"""

Created on Tue Jan 17 13:55:42 2023

@author: patiwa danny mhango.
@Email : patiwadannymhango@outlook.com
@Github: patiwadannymhango


"""

import pandas as pd
import numpy as np
import sqlalchemy as sql



def openConnection(driver,username,password,server,instance,db):
    '''
    Creates a DB connection 

    Args
    -----
    driver : Exanple ODBC Driver 17 for SQL Server
    username : Login Username.
    password : Login Password.
    Server : The Server IP Address or Alias
    instance: Instance Name.
    db: Database.

    Returns
    -------
    SQlAlchemy Engine Connection.

    '''
    connection = sql.create_engine(
        f"mssql+pyodbc://{username}:{password}@{server}{instance}/{db}?driver={driver}", fast_executemany=True
    )
    return connection

def closeConnection(connection):
    '''
    Closes the DB Connection.
    Args
    -----
    connection : DB Connection

    Returns
    -------
    SQlAlchemy Engine Connection.

    '''
    connection.dispose()



def getAvgPIdataRange(tags, startDT, endDT , interval, connection, piAddressName):
    '''
    Retrieves historised process data from the PI historian
    Args
    -----
    tags : array_like
        List of tags or PI points for which data should be retrieved.
    startDT : datetime
        Start time for tag data retrieval '2018-01-01 05:01'
    endDT : datetime
        End time for tag data retrieval '2018-01-02 05:30'
    dataInterval : char
        The interval by which successive data points will be separated
        '1s' = 1 second
        '10s' = 10 seconds
        '5m' = 5 minutes
        '1h' = 1 hour
        '1d' = 1 day
    connection: sql connection
    piAddressName:IP Address of the PI ARCHIVE Instance.

    Returns
    -------
    df : Pandas Date Frame
        Date frame of time series data with columns for each tag/point
    '''

    df = pd.DataFrame()

    try:
        tags = tuple(tags)
        sql = ( f''' SELECT * FROM OPENQUERY({piAddressName}, 
                    'SELECT tag, time as sampleDateTime , value 
                     FROM [piarchive]..[piavg]
                     WHERE tag in (''{"'',''".join(map(str, tags))}'') 
                     AND time BETWEEN ''{startDT }'' AND ''{endDT }'' 
                     AND timestep = ''{interval}''
                    ')''')
                    
        df = pd.read_sql(sql, connection)

    except Exception as ex:
        print(ex)
        pass
    
    closeConnection(connection)


    return(df)



def getPivotAvgPIdataTimeDT(tags,timeDT, interval, connection, piAddressName):
    '''
    Retrieves historised process data from the PI historian
    Args
    ----
    tags : array_like
        List of tags or PI points for which data should be retrieved.
    timeDT : datetime
        Start time for tag data retrieval '2018-01-01 05:01'
  
    dataInterval : char
        The interval by which successive data points will be separated
        '1s' = 1 second
        '10s' = 10 seconds
        '5m' = 5 minutes
        '1h' = 1 hour
        '1d' = 1 day
    connection: sql connection
    piAddressName:IP Address of the PI ARCHIVE Instance.
    Returns
    -------
    df : Pandas Date Frame
        Date frame of time series data with columns for each tag/point
    '''

    df = pd.DataFrame()

    try:
        tags = tuple(tags)
        sql = ( f''' SELECT * FROM OPENQUERY({piAddressName}, 
                    'SELECT tag, time as sampleDateTime , value 
                     FROM [piarchive]..[piavg]
                     WHERE tag in (''{"'',''".join(map(str, tags))}'') 
                     AND time = ''{timeDT}'' 
                     AND timestep = ''{interval}''
                    ')''')
                    
        df = pd.read_sql(sql, connection)
        
    except Exception as ex:
        print(ex)
        pass

    closeConnection(connection)
    
    return(df)


def getPivotAvgPIdataRange(tags, startDT, endDT , interval, connection, piAddressName):
    '''
    Retrieves historised process data from the PI historian
    Args
    -----
    tags : array_like
        List of tags or PI points for which data should be retrieved.
    startDT : datetime
        Start time for tag data retrieval '2018-01-01 05:01'
    endDT : datetime
        End time for tag data retrieval '2018-01-02 05:30'
    dataInterval : char
        The interval by which successive data points will be separated
        '1s' = 1 second
        '10s' = 10 seconds
        '5m' = 5 minutes
        '1h' = 1 hour
        '1d' = 1 day
    connection: sql connection
    piAddressName:IP Address of the PI ARCHIVE Instance.

    Returns
    -------
    df : Pandas Date Frame
        Date frame of time series data with columns for each tag/point
    '''

    df = pd.DataFrame()
    dfTemp = pd.DataFrame()
    dfTemp2 = []

    try:
        tags = tuple(tags)
        sql = ( f''' SELECT * FROM OPENQUERY({piAddressName}, 
                    'SELECT tag, time as sampleDateTime , value 
                     FROM [piarchive]..[piavg]
                     WHERE tag in (''{"'',''".join(map(str, tags))}'') 
                     AND time BETWEEN ''{startDT }'' AND ''{endDT }'' 
                     AND timestep = ''{interval}''
                    ')''')
                    
        dfTemp = pd.read_sql(sql, connection)
        dfTemp.value = pd.to_numeric(dfTemp.value)
        dfTemp = dfTemp.pivot(index='sampleDateTime', columns='tag', values='value')
        
        dfTemp2.append(dfTemp)
        

    except Exception as ex:
        print(ex)
        connection.close()
        pass

    df = pd.concat(dfTemp2)

    if not df.empty:
        df.index = df.index.astype('datetime64[ns]')
      
    closeConnection(connection)
    
    return(df)



def getPivotAvgPIdataTimeDT(tags,timeDT, interval, connection, piAddressName):
    '''
    Retrieves historised process data from the PI historian
    Args
    ----
    tags : array_like
        List of tags or PI points for which data should be retrieved.
    timeDT : datetime
        Start time for tag data retrieval '2018-01-01 05:01'
  
    dataInterval : char
        The interval by which successive data points will be separated
        '1s' = 1 second
        '10s' = 10 seconds
        '5m' = 5 minutes
        '1h' = 1 hour
        '1d' = 1 day
    connection: sql connection
    piAddressName:IP Address of the PI ARCHIVE Instance.
    Returns
    -------
    df : Pandas Date Frame
        Date frame of time series data with columns for each tag/point
    '''

    df = pd.DataFrame()
    dfTemp = pd.DataFrame()
    dfTemp2 = []

    try:
        tags = tuple(tags)
        sql = ( f''' SELECT * FROM OPENQUERY({piAddressName}, 
                    'SELECT tag, time as sampleDateTime , value 
                     FROM [piarchive]..[piavg]
                     WHERE tag in (''{"'',''".join(map(str, tags))}'') 
                     AND time = ''{timeDT}'' 
                     AND timestep = ''{interval}''
                    ')''')
                    
        dfTemp = pd.read_sql(sql, connection)
        dfTemp.value = pd.to_numeric(dfTemp.value)
        dfTemp = dfTemp.pivot(index='sampleDateTime', columns='tag', values='value')
        
        dfTemp2.append(dfTemp)
        

    except Exception as ex:
        print(ex)
        connection.close()
        pass

    df = pd.concat(dfTemp2)

    if not df.empty:
        df.index = df.index.astype('datetime64[ns]')
      
    closeConnection(connection)

    return(df)







