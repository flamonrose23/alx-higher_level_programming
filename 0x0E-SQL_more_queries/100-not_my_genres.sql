-- Writing script using hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.name NOT IN
      (SELECT x.name AS name
      FROM tv_genres AS x
      JOIN tv_show_genres AS y
      ON y.genre_id = x.id
      JOIN tv_shows AS z
      ON y.show_id = z.id
      WHERE z.title = 'Dexter')
ORDER BY tv_genres.name ASC;
