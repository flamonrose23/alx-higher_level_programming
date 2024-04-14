#!/usr/bin/python3
"""
Script listsing all states from database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    curt = db.cursor()
    curt.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = curt.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    curt.close()
    db.close()
