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
    Siblings_Spouses_Aboard int, 
    Parents_Children_Aboard int, 
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
WHERE Survived = 0;
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
WHERE Pclass = 1
AND Survived =1;
''')

Pclass_thing1_survived = cursor.fetchall()
print("people who survived in class 1", Pclass_thing1_survived)

cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 2
AND Survived =1;
''')

Pclass_thing2_survived = cursor.fetchall()
print("people who survived in class 2", Pclass_thing2_survived)

cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 3
AND Survived =1;
''')

Pclass_thing3_survived = cursor.fetchall()
print("people who survived in class 3", Pclass_thing3_survived)

#########################################################
cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 1
AND Survived =0;
''')
Pclass_thing1_survived = cursor.fetchall()
print("people who died in class 1", Pclass_thing1_survived)

cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 2
AND Survived =0;
''')

Pclass_thing2_survived = cursor.fetchall()
print("people who died in class 2", Pclass_thing2_survived)

cursor.execute('''SELECT COUNT(Pclass)
FROM titanic_table
WHERE Pclass = 3
AND Survived =0;
''')

Pclass_thing3_survived = cursor.fetchall()
print("people who died in class 3", Pclass_thing3_survived)

#############################################################
cursor.execute('''SELECT AVG(Age)
FROM titanic_table
WHERE Survived = 1;
''')

avg_age = cursor.fetchall()
print("average age of survivors: ", avg_age)

cursor.execute('''SELECT AVG(Age)
FROM titanic_table
WHERE Survived = 0;
''')

avg_age2 = cursor.fetchall()
print("average age of the dead: ", avg_age2)

#############################################################
#What was the average age of each passenger class

cursor.execute('''SELECT AVG(Age)
FROM titanic_table
WHERE Pclass = 1;
''')

avg_Pclass1 = cursor.fetchall()
print("average age of Pclass 1: ", avg_Pclass1)

cursor.execute('''SELECT AVG(Age)
FROM titanic_table
WHERE Pclass = 2;
''')

avg_Pclass2 = cursor.fetchall()
print("average age of Pclass 2: ", avg_Pclass2)

cursor.execute('''SELECT AVG(Age)
FROM titanic_table
WHERE Pclass = 3;
''')

avg_Pclass3 = cursor.fetchall()
print("average age of Pclass 3: ", avg_Pclass3)

#############################################################
cursor.execute('''SELECT AVG(Fare)
FROM titanic_table
WHERE Pclass = 1;
''')

avg_fare_pclass1 = cursor.fetchall()
print("average Fare of Pclass 1: ", avg_fare_pclass1)

cursor.execute('''SELECT AVG(Fare)
FROM titanic_table
WHERE Pclass = 2;
''')

avg_fare_pclass2 = cursor.fetchall()
print("average Fare of Pclass 2: ", avg_fare_pclass2)

cursor.execute('''SELECT AVG(Fare)
FROM titanic_table
WHERE Pclass = 3;
''')

avg_fare_pclass3 = cursor.fetchall()
print("average Fare of Pclass 3: ", avg_fare_pclass3)

###############################################################
cursor.execute('''SELECT AVG(Fare)
FROM titanic_table
WHERE Survived = 1;
''')

avg_fare_survival1 = cursor.fetchall()
print("average Fare of Survived: ", avg_fare_survival1)

cursor.execute('''SELECT AVG(Fare)
FROM titanic_table
WHERE Survived = 0;
''')

avg_fare_survival0 = cursor.fetchall()
print("average Fare of Dead: ", avg_fare_survival0)

################################################################
cursor.execute('''SELECT AVG(Siblings_Spouses_Aboard)
FROM titanic_table
WHERE Pclass = 1;
''')

avg_siblings1 = cursor.fetchall()
print("average Siblings and Spouses aboard in Pclass 1: ", avg_siblings1)

cursor.execute('''SELECT AVG(Siblings_Spouses_Aboard)
FROM titanic_table
WHERE Pclass = 2;
''')

avg_siblings2 = cursor.fetchall()
print("average Siblings and Spouses aboard in Pclass 2: ", avg_siblings2)

cursor.execute('''SELECT AVG(Siblings_Spouses_Aboard)
FROM titanic_table
WHERE Pclass = 3;
''')

avg_siblings3 = cursor.fetchall()
print("average Siblings and Spouses aboard in Pclass 3: ", avg_siblings3)
###################################################################

cursor.execute('''SELECT AVG(Siblings_Spouses_Aboard)
FROM titanic_table
WHERE Survived = 1;
''')

survived_siblings1 = cursor.fetchall()
print("average Siblings and Spouses aboard Survived: ", survived_siblings1)


cursor.execute('''SELECT AVG(Siblings_Spouses_Aboard)
FROM titanic_table
WHERE Survived = 0;
''')

survived_siblings0 = cursor.fetchall()
print("average Siblings and Spouses aboard dead: ", survived_siblings0)
########################################################################
cursor.execute('''SELECT AVG(Parents_Children_Aboard)
FROM titanic_table
WHERE Pclass = 1;
''')

Parent_Child_avg1 = cursor.fetchall()
print("average parent and child aboard in Pclass 1: ", Parent_Child_avg1)

cursor.execute('''SELECT AVG(Parents_Children_Aboard)
FROM titanic_table
WHERE Pclass = 2;
''')

Parent_Child_avg2 = cursor.fetchall()
print("average parent and child aboard in Pclass 2: ", Parent_Child_avg2)

cursor.execute('''SELECT AVG(Parents_Children_Aboard)
FROM titanic_table
WHERE Pclass = 3;
''')

Parent_Child_avg3 = cursor.fetchall()
print("average parent and child aboard in Pclass 3: ", Parent_Child_avg3)
######################################################################
cursor.execute('''SELECT AVG(Parents_Children_Aboard)
FROM titanic_table
WHERE Survived = 1;
''')

Parent_Child_survived1 = cursor.fetchall()
print("average Siblings and Spouses aboard Survived: ", Parent_Child_survived1)

cursor.execute('''SELECT AVG(Parents_Children_Aboard)
FROM titanic_table
WHERE Survived = 0;
''')

Parent_Child_survived0 = cursor.fetchall()
print("average Siblings and Spouses aboard dead: ", Parent_Child_survived0)

##########################################################################
cursor.execute('''SELECT Name FROM titanic_table
ORDER BY Name
LIMIT 50;

''')

same_name = cursor.fetchall()
print("yes there are some: ", same_name)




cursor.close()
connection.commit()
connection.close()