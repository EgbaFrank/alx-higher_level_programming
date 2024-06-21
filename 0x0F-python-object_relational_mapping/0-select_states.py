#!/usr/bin/python3
"""
This module is a script that lists all states
from the database hbtn_0e_0_usa
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
                db=sys.argv[3])
        cur = db.cursor()

        cur.execute("SELECT * FROM states ORDER BY id ASC")
        states = cur.fetchall()

        for row in states:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        cur.close()
        db.close()
