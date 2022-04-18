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
    # from markupsafe import escape
    # Right way (+ escape)
    # author = author[:128]
    # text = text[:512]
    # author = escape(author)
    # text = escape(text)
    # conn.cursor().execute(
    #     "INSERT INTO feedback (author, text) VALUES (?, ?);",
    #     (author, text)
    # )
    author = sanitize(author)
    text = sanitize(text)
    author = author[:128]
    text = text[:512]
    query = "INSERT INTO blog (author, text) VALUES ('{}', '{}');".format(
        author, text
    )
    conn.cursor().executescript(query)
    print("Saved blog {}: {}".format(author, text))


def get_all_blogs():
    cursor = conn.cursor()
    cursor.execute("SELECT author, text FROM blog;")
    return cursor.fetchall()


def sanitize(s):
    return s.replace("'", "''")
