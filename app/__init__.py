"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaaet2k728r886dtae0-a.oregon-postgres.render.com",
        database="todo_it5m",
        user="todo_it5m_user",
        password="nILgJ53zjzrt3ONBwfs0EXR38H6CS6Mg")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
