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

        cur.execute("SELECT cities.name\
                     FROM cities\
                     WHERE state_id = (SELECT id\
                                       FROM states\
                                       WHERE name = %s\
                                )\
                     ORDER BY cities.id ASC", (sys.argv[4],)
                    )
        cities = cur.fetchall()

        city_names = [record[0] for record in cities]
        fmt_str = ', '.join(city_names)

        print(fmt_str)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        cur.close()
        db.close()
