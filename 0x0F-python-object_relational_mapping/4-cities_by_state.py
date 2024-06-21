#!/usr/bin/python3
"""
This module contains a script that
lists all cities from the database
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

        cur.execute("SELECT cities.id,\
                        cities.name,\
                        states.name\
                     FROM cities\
                     INNER JOIN states\
                     ON states.id = cities.state_id\
                     ORDER BY cities.id ASC")

        cities = cur.fetchall()

        for record in cities:
            print(record)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        cur.close()
        db.close()
