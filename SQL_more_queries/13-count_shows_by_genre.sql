-- we use where command inside a where command to take information out of other tables
SELECT tv_genres.name,COUNT(tv_show_genres.show_id) AS occurence 
FROM tv_genres,tv_shows
JOIN tv_show_genres
ON  tv_genres.id=tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY tv_genres.name
ORDER BY  occurence DESC;
