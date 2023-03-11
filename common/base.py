from sqlalchemy import create_engine
import os
import cx_Oracle 

def connection_oracle():

    cx_Oracle.init_oracle_client(r'C:\oracle\instantclient_19_17')

    username= "********"
    password= "********"
    dialect= "oracle"
    sql_driver ="cx_oracle"
    hostname= "********"
    port= "1521"
    service= "ORCL"

    path_win_auth= dialect + '+' + sql_driver + '://' + username + ':' +\
    password +'@' + hostname + ':' + str(port) + '/?service_name=' + service

    engine = create_engine(path_win_auth)

    print(path_win_auth)

    return engine


def connection_sqlite():

    path_win_auth = 'sqlite:///D:/DB/DB-Sqlite/db-sql_lite.db'
    engine = create_engine(path_win_auth)  
    
    return engine
