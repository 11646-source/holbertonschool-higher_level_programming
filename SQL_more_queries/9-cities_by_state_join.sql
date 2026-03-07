-- Lists all cities of california from the database htbn_0d_usa
-- Usage: mysql -u root -p <database_name> < script.sql

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
