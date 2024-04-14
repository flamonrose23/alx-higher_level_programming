#!/usr/bin/python3

import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # maing connection to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # giving the ability to have multiple seperate working environments
    # through same connection to the database.
    curt = db.cursor()

    curt.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = curt.fetchall()
    for x in rows:
        print(x)
    # Clean up process
    curt.close()
    db.close()
