-- A script that lists all shows contained in hbtn_0d_tvshows that may have a genre or not
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
