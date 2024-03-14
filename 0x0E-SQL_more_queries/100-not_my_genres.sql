-- Writing script using hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.name NOT IN
      (SELECT a.name AS name
      FROM tv_genres AS a
      JOIN tv_show_genres AS b
      ON b.genre_id = a.id
      JOIN tv_shows AS c
      ON b.show_id = c.id
      WHERE c.title = 'Dexter')
ORDER BY tv_genres.name ASC;
