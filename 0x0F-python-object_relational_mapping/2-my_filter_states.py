#!/usr/bin/python3
"""
This module contains database record
search functionality
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
                port=3306,
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
    )
    cur = db.cursor()

    cur.execute("SELECT *\
                 FROM states\
                 WHERE name = '{}'\
                 ORDER BY id ASC".format(sys.argv[4]))
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()
