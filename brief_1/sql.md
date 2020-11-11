SELECT user, host, plugin, authentication_string FROM mysql.user;
CREATE USER 'myriam'@'localhost' IDENTIFIED BY 'hey';
create database cardb;
GRANT ALL ON *.* TO 'myriam'@'localhost';

------



from sqlalchemy import create_engine
import pymysql
import pandas as pd

# Connecting to MySQL server at localhost using PyMySQL DBAPI 
sqlEngine = create_engine("mysql+pymysql://anne:password@localhost/db_car")
dbConnection = sqlEngine.connect()
frame = pd.read_sql("select * from db_car.cardata", dbConnection);
dbConnection.close()

----

import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://julien:julien@localhost/cardb')
car_data.to_sql('cardata', engine)

-----


import mysql.connector

cnx = mysql.connector.connect(user='anne', password='mea31177',
                              host='127.0.0.1',
                              database='db_car')


if cnx.is_connected():
    db_Info = cnx.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = cnx.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

sql_select_Query = "select * from cardata"
cursor = cnx.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Total number of rows in Laptop is: ", cursor.rowcount)

print("\nPrinting each laptop record")
for row in records:
    print("Car_Name = ", row[0], )
    print("Year = ", row[1])
    print("Selling_Price  = ", row[2])
    print("Present_Price  = ", row[3], "\n")

cnx.close()