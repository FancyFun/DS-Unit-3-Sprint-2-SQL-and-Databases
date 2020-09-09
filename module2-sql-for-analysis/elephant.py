import psycopg2
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                        password = DB_PASSWORD, host = DB_HOST)
connection2 = sqlite3.connect('rpg_db.sqlite3')

cursor2 = connection2.cursor()
cursor = connection.cursor()

cursor2.execute('''SELECT item_ptr_id, power FROM armory_weapon''');

result2 = cursor2.fetchall()

cursor.execute('''CREATE TABLE test_table (item_ptr_id int, power int);
''')

for results in result2:
    cursor.execute(f'''INSERT INTO test_table (item_ptr_id, power)
    VALUES ({results[0]}, {results[1]}) ''')

cursor.close()
connection.commit()
connection.close()