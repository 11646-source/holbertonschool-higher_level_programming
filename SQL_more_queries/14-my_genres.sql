-- Script to list all genres of the show Dexter
-- Usage: mysql -u <username> -p <database_name> < script.sql

SELECT g.name AS genre
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON s.id = sg.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
