-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title, SUM(ratings.rating) AS total_rating
FROM tv_shows
INNER JOIN ratings ON tv_shows.id = ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY total_rating DESC;
