#!/usr/bin/python3
"""
This module contains database record
search functionality
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

        cur.execute(f"SELECT *\
                     FROM states\
                     WHERE name = '{sys.argv[4]}'\
                     ORDER BY id ASC")
        states = cur.fetchall()

        for row in states:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        cur.close()
        db.close()
