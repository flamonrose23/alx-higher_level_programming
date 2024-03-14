-- Writing script listing all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating

SELECT x.name, SUM(z.rate) AS rating FROM tv_genres AS x
JOIN tv_show_genres AS y ON x.id = y.genre_id
JOIN tv_show_ratings AS z ON y.show_id = z.show_id
GROUP BY x.name ORDER BY rating DESC;
