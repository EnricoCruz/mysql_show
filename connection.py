#installed mysql version 8.*
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd="toor",
    database='sakila'
)
