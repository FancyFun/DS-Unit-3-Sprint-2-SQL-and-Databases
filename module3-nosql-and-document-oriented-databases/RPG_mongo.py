import sqlite3
import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://JKMHensiek:password@cluster0.98jkv.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

connection = sqlite3.connect('rpg_db.sqlite3')

cursor = connection.cursor()

cursor.execute('''
SELECT character_ptr_id, using_shield, rage FROM charactercreator_fighter
''')
rpg_character = cursor.fetchall() 

rpg_doc = {
    'sql_key' : rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
}
db.test.insert_one(rpg_doc)

print(list(db.test.find()))

##In comparison this way to me is a lot easier.
## I have a website to connect to. I can place the data into the table 
## easier and it doesn't require a for loop. The hardest thing I can think
## of with this section is the library. They are a little confusing but 
## it gets easier with more practice. 
