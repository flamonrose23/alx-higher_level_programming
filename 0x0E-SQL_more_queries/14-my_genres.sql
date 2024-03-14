-- Writing script using hbtn_0d_tvshows database to lists all genres of the show Dexter
-- tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT tv_genres.name FROM tv_show_genres INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter" ORDER BY tv_genres.name ASC;
