-- Script: 11-list_shows.sql
-- Lists all shows contained in the database htbn_0d_tvshows

SELECT tv_shows.title
FROM tv_shows
ORDER BY tv_shows.title ASC;
