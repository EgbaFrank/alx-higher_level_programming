-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows
WHERE NOT EXISTS (
	SELECT 1
	FROM tv_show_genres
	INNER JOIN tv_genres
		ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_shows.id = tv_show_genres.show_id
		AND tv_genres.name = 'Comedy'
)
ORDER BY title;
