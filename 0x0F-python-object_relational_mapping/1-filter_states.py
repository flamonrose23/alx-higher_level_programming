#!/usr/bin/python3
"""  listing all states from database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curent = db.cursor()
    curent.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = curent.fetchall()
    for row in rows:
        print(row)
    curent.close()
    db.close()
