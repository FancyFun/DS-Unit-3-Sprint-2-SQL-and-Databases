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

cursor2.execute('''SELECT Survived, Pclass, name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare FROM titanic''')

result2 = cursor2.fetchall()

cursor.execute('''DROP TABLE IF EXISTS titanic_table; 
    CREATE TABLE IF NOT EXISTS titanic_table ( 
    Survived int, 
    Pclass int, 
    name text, 
    Sex text, 
    Age int, 
    Siblings_Spouses_Aboard text, 
    Parents_Children_Aboard text, 
    Fare float
); 

''')

for results in result2:
    cursor.execute(f'''INSERT INTO titanic_table (Survived, Pclass, name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES ({results[0]}, {results[1]}, '{results[2].replace("'", "`")}', '{results[3]}', {results[4]}, {results[5]}, {results[6]}, {results[7]})''') 
cursor.close()
connection.commit()
cursor = connection.cursor()

cursor.execute('''SELECT COUNT(Survived)
FROM titanic_table
WHERE Survived = 1;
''')

survived = cursor.fetchall()
print("This many people Survived: ", survived)

cursor.execute('''SELECT COUNT(Survived)
FROM titanic_table
WHERE Survived = 1;
''')

died = cursor.fetchall()
print("This many people died: ", died)

cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 1;
''')

Pclass_thing1 = cursor.fetchall()
print("people in class 1", Pclass_thing1)

cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 2;
''')

Pclass_thing2 = cursor.fetchall()
print("people in class 2", Pclass_thing2)

cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 3;
''')

Pclass_thing3 = cursor.fetchall()
print("people in class 3", Pclass_thing3)

cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 3
AND Survived =1;
''')

Pclass_thing3_survived = cursor.fetchall()
print("people who survived in class 3", Pclass_thing3_survived)

cursor.close()
connection.commit()
connection.close()