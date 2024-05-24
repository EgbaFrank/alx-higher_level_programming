--  list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE NOT EXISTS (
	SELECT 1
	FROM tv_show_genres
	INNER JOIN tv_shows
		ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_show_genres.genre_id = tv_genres.id
	AND tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
