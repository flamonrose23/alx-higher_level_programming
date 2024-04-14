#!/usr/bin/python3
import MySQLdb
from sys import argv

# The code should not executed when it is imported
if __name__ == '__main__':
    # connection to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # ability to have multiple seperate working environments
    # through same connection t database.
    curent = db.cursor()

    curent.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = curent.fetchall()
    for x in rows:
        print(x)
    # Clean all process
    curent.close()
    db.close()
