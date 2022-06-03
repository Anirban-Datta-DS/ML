import numpy as np
import pandas as pd
import pyodbc 
import getpass
import pandas.io.sql

for driver in pyodbc.drivers():
    print(driver)

server = 'IN3074556W1' 
database = 'Advanced_Analytics' 
username = input(" Enter username: ")
password = getpass.getpass(" Enter Password: ")

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                       SERVER='+server+';\
                       DATABASE='+database+';\
                       Trusted_Connection=yes;')


cursor = cnxn.cursor()

read='select * from ConsumerElectronics'
# directly read into dataframe
df_Consumer_electronics= pandas.io.sql.read_sql(read, cnxn)

print(df_Consumer_electronics.head(3))
cnxn.close()