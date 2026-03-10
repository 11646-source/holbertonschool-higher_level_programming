#!/usr/bin/python3
"""
Lists all cities from database htbn_0e_4_usa.
Arguments: mysql username, mysql password, database name.
"""

import MYSQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # conect to MySQL
    db = MySQLdb.connect(
         host="localhost",
         port=3306,
         user=username,
         passwd=password
         db=db_name
    )

    cursor = db.cursor()

     # Execute query (only once)
     cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON cities.states_id = states.id \
                    ORDER BY cities.id ASC")
     # Display results
     for row in cursor.fetchall():
         print(row)
         # Close resources
         cursor.close()
         db.close()

