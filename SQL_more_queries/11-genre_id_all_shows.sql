-- Lists all shows contained in hbtn_0d_tvshows with their genre_id
-- Each record shows: tv_shows.title - tv_show_genres.genre_id
-- Includes shows with no genre (NULL)
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
