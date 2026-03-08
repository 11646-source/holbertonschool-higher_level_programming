-- Lists all genres of the show Dexter
-- Usage: mysql -u root -p <database_name> < 14-my_genres.sql

SELECT g.name AS name
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON s.id = sg.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
