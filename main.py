from os import name
import sqlite3
from sqlite3.dbapi2 import Cursor
import sys

connection = sqlite3.connect("people.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people (name TETX, age INTEGER, skills STRING)")
except Exception as e:
    pass

def user_is_unique(name):
    rows = cursor.execute("SELECT name, age, skills FROM pepole").fetchall()

    for user in rows:
        if user[0] == name:
            return False
    return True

def insert_db():
    name = input("Name >>")

    if user_is_unique(str(name)):
        age = input("Age >>")
        skills = input("Skills >>")

        if name !="" and age != "" and skills != "":
            cursor.execute(f"INSER INTO people VALUES ('{name}', '{age}', '{skills}')")
            connection.commit()
            print(name + " has been added to the database!")

        else:
            print("One of the fields are empty!")
            insert_db()
    else:
        print("Name is already in the database!")

def edit_db():
    name = input("Type name of the person you would like to edit")
    
