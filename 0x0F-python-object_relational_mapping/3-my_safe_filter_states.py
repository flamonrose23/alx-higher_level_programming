#!/usr/bin/python3

"""
Script taking arguments and displaying all values in table of hbtn_0e_0_usa
By writing one safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    curt = db.cursor()
    match = sys.argv[4]
    curt.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = curt.fetchall()
    for row in rows:
        print(row)
    curt.close()
    db.close()
