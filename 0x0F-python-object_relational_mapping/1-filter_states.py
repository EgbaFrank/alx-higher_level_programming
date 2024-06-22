#!/usr/bin/python3
"""
this module contains a
script that lists all states
with a name starting with N
"""
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
                    port=3306,
                    host="localhost",
                    user=sys.argv[1],
                    passwd=sys.argv[2],
                    db=sys.argv[3]
        )
        cur = db.cursor()

        cur.execute("SELECT * FROM states\
                     WHERE name LIKE BINARY 'N%'\
                     ORDER BY id ASC")
        states = cur.fetchall()

        for row in states:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        cur.close()
        db.close()
