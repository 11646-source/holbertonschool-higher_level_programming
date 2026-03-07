-- Lists all cities of California from the database hbtn_0d_usa
-- Usage: mysql -u root -p <database_name> < script.sql

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
