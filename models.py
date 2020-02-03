import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    #establish connection to DB
    con = sql.connect(path.join(ROOT, 'database.db'))
    #create cusor so we dont retrieve the whole database just the info we want
    cur = con.cursor()
    #execute this SQL syntax
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    #establish connection to DB
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    #select all posts from db
    cur.execute('select * from posts')
    #store all the posts in the posts variable
    posts = cur.fetchall()
    return posts


