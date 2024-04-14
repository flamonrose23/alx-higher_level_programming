#!/usr/bin/python3
"""
Script listing all cities from database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db=argv[3])

    with db.cursor() as curt:
        curt.execute("""SELECT cities.id, cities.name, states.name
            FROM cities JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC""")
        rows = curt.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
