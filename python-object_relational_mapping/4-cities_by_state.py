#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Collect arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Execute query (only once)
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    # Display results
    for row in cursor.fetchall():
        print(row)

    # Close resources
    cursor.close()
    db.close()
