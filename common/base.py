from sqlalchemy import create_engine,MetaData
import os
import cx_Oracle


def connection_oracle_sqlalchemy():  

    # #Definindo PATH Client
    cx_Oracle.init_oracle_client(config_dir="/opt/oracle/instantclient_19_17")


    username= "**********"
    password= "**************"
    dialect= "oracle"
    sql_driver ="cx_oracle"
    hostname= "************"
    port= "**********"
    service= "ORCL"

    path_win_auth= dialect + '+' + sql_driver + '://' + username + ':' +\
    password +'@' + hostname + ':' + str(port) + '/?service_name=' + service

    engine = create_engine(path_win_auth)


    return engine


def spark_init():
    """_Init Spark in Vscode_
    """

    import findspark

    findspark.init('/opt/spark/')

    from pyspark.sql import SparkSession

    spark = SparkSession.builder\
        .master('local[*]')\
        .appName('Spark-Vscode')\
        .getOrCreate() 

    return spark
