#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Takes 4 arguments: mysql username, mysql password, database name, and state name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()

    # Safe query (SQL injection free)
    cursor.execute("SELECT cities.id, cities.name \
                    FROM cities JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name,))

    rows = cursor.fetchall()

    # Extract only city names
    city_names = [row[1] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
