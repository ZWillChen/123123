# **B**attery**L**earn

- [batterydata](#batterydata)
  * [supported datasources](#supported-datasources)
  * [examples](#examples)    
    + [mysql](#mysql)
    + [influxdb](#influxdb)
  * [api](#api)
- [batterydocs](#batterydocs)
  * [file format](#file-format)
  * [examples](#examples-1)    
    + [sharepoint](#sharepoint)
- [batterylearn](#batterylearn)
  * [Install](#install)
- [batterygui](#batterygui)
  * [Install](#install)


## BatteryData
> class that handle the in and out of Battery data and documents to database
### Supported Datasources
> MS Sharepoint, Mysql, influxdb
### examples
#### mysql
> example wip
#### influxdb

> Query and download data from Gotion influxDB
```python
import os
import pandas as pd
from influxdb import DataFrameClient

host='sw-wus-hx501q2'
port=8086

"""Instantiate the connection to the InfluxDB client."""
user = 'data_user'
password = '*****'
protocol = 'line'
dbname = 'Vehicle'

client = DataFrameClient(host, port, user, password, dbname)

""" setting the query"""
q = 'SELECT first("动力电池剩余电量SOC") AS "SOC",\
    first("动力电池充/放电电流") AS "current" \
    FROM LNBSCB3F1KW003004 \
    WHERE time >= now() - 90d \
    GROUP BY time(10m) fill(null)'

""" execute the query"""
get1= client.query(q)

""" fetch the measrurement content"""
get1.get('LNBSCB3F1KW003004')

```

> upload data to the Gotion influxDB

```python
# upload pandas dataframe object

from BatteryData import upload_to_influxdb

df1 = df.set_index('时间')
upload_to_influxdb(df1,'test',measurement-name,False)

```
### api
> example wip

## BatteryDocs
> classes that handle design time-series data, documentations, requirements and tables
### file format
> *.csv, *.xlsx, *.mdf, *.docx
### examples
#### sharepoint
> example wip


## BatterLearn
> classes that simulate and analyze battery data
> battery modeling, simulation, Kalman filter, machine learning


## BatteryGUI
> GUI for using the above functionalities
### client-gui
### webbased 
### Install
To install all requirements necessary for running the GUI, run the following code in the command line:
```
python -m pip install -r requirements.txt
```
> (Django/Flask)