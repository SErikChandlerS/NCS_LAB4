from mysql import connector
import mysql
from flask import Flask, g
app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'site'
    }
conn = mysql.connector.connect(**config)

def post_in_blog(author, text):

    """to fix the vulnerability use commented code"""
    # from markupsafe import escape
    # author = author[:128]
    # text = text[:512]
    # author = escape(author)
    # text = escape(text)
    # conn.cursor().execute(
    #     "INSERT INTO feedback (author, text) VALUES (?, ?);",
    #     (author, text)
    # )
    author = reformat(author)
    text = reformat(text)
    query = "INSERT INTO blog (author, text) VALUES ('{}', '{}');".format(
        author, text
    )
    conn.cursor().executescript(query)


def get_all_blogs():
    cursor = conn.cursor()
    cursor.execute("SELECT author, text FROM blog;")
    return cursor.fetchall()


def reformat(s):
    return s.replace("'", "''")
