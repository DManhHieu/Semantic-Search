import mysql.connector
import os

host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
user = os.getenv('MYSQL_USER')
pwd = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

def connection():
    return mysql.connector.connect(host = host,
                      user = user,
                      passwd = pwd,
                      db = database
                    )