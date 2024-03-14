-- Writing script listing all shows without genre Comedy in database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy
-- Results must be sorted in ascending order by the show title

SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.title NOT IN
      (SELECT x.title
      FROM tv_shows AS x
      JOIN tv_show_genres AS y
      ON x.id = y.show_id
      JOIN tv_genres AS z
      ON y.genre_id = z.id
      WHERE z.name = 'Comedy')
ORDER BY tv_shows.title ASC;
