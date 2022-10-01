import sqlite3


INSERT_P="INSERT INTO PRODUCT(NAME,PRICE,RATING) VALUES(?,?,?)"

get_AllP="SELECT * FROM PRODUCT;"
get_PName="SELECT * FROM PRODUCT WHERE NAME=?;"
get_TopR="""
SELECT * FROM PRODUCT
ORDER BY RATING DESC;
"""

get_P_ByPrice="""
SELECT * FROM PRODUCT
ORDER BY PRICE ASC;
"""

def conn():
    return sqlite3.connect("pdata.db")

def createTable(conn):
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCT
            (ID INTEGER PRIMARY KEY,
            NAME TEXT NOT NULL,
            PRICE INT NOT NULL,
            RATING INT NOT NULL);''')

def insertP(conn,NAME,PRICE,RATING):
    with conn:
        conn.execute(INSERT_P,(NAME,PRICE,RATING))

def getAllP(conn):
    with conn:
        return conn.execute(get_AllP).fetchall()

def getPName(conn,NAME):
    with conn:
        return conn.execute(get_PName,(NAME,)).fetchall()

def getTopP(conn):
    with conn:
        return conn.execute(get_TopR).fetchall()

def getPByPrice(conn):
    with conn:
        return conn.execute(get_P_ByPrice)
