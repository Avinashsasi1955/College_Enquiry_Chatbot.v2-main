import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Rohit#0408",
        database="college_chatbot"
    )
