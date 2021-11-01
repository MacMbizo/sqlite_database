import sqlite3
from sqlite3.dbapi2 import Cursor
import sys

connection = sqlite3.connect("people.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people (name TETX, age INTEGER, skills STRING)")
except Exception as e:
    pass

