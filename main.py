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
            cursor.execute(f"INSERT INTO people VALUES ('{name}', '{age}', '{skills}')")
            connection.commit()
            print(name + " has been added to the database!")

        else:
            print("One of the fields are empty!")
            insert_db()
    else:
        print("Name is already in the database!")

def edit_db():
    name = input("Type name of the person you would like to edit")
    field = input("Which field would you like to edit: name, age, or skills? >>")
    updated_field = input ("What would you like to update it to? >>")

    try:
        cursor.execute(f"UPDATED people SET {field} = ? WHERE name = ?", (updated_field, name))
        connection.commit()
        print("Successfully updated user!")
    except Exception as e:
        print(e)

def get_user_info_db():
    target_name = input("Who do you wnat to see information about? >>")
    rows = cursor.execute("SELECT name,age,skills FROM people WHERE name = ?", (target_name),).fetchall()

    name = rows[0][0]
    age = rows [0][1] # rows [(name, age, skills)]
    skills = rows [0][2]

    print (f"{name} is {age} years old, and works as a {skills}.")


