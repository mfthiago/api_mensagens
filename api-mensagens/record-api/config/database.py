import mysql.connector

def get_db():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='chat'
    )
