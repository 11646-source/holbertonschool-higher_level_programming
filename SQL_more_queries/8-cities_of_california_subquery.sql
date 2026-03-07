#!/bin/bash
# Lists all cities of California from the database hbtn_0d_usa
# Usage: ./script.sh <database_name>

mysql -u root -p "$1" -e "
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
"
