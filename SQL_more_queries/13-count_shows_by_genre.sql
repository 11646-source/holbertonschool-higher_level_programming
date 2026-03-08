-- Script to list all genres and the number of shows linked to each
-- Usage: mysql -u <username> -p <database_name> < script.sql

SELECT g.name AS genre,
       COUNT(sg.show_id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
GROUP BY g.name
HAVING COUNT(sg.show_id) > 0
ORDER BY number_of_shows DESC;
