#!/usr/bin/python3
"""
Writing Script listing all states from database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    curent = db.cursor()
    curent.execute("SELECT * FROM states")

    rows = curent.fetchall()
    for x in rows:
        print(x)
    curent.close()
    db.close()
