-- lists all shows contained in hbtn_0d_tvshows
-- shows linked to each other
-- order display
SELECT g.name AS genre
	count(*) AS number_of_shows
 FROM tv_genres AS g
      	INNER JOIN tv_show_genres AS t
        ON g.id = t.genre_id
 GROUP BY g.name
 ORDER BY number_of_shows DESC;
