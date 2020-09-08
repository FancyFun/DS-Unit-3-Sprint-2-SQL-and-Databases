import psycopg2
import os
from dotenv import load_dotenv

DB_NAME = 'mydqblep'
DB_USER = 'mydqblep'
DB_PASSWORD = 'CstliUgtN8dt1csStj7CeXfov7m3-g5e'
DB_HOST = 'lallah.db.elephantsql.com'

connection = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASSWORD, host = DB_HOST)

cursor = connection.cursor()

cursor.execute('SELECT * FROM test_table;')

result = cursor.fetchall()
print(result)