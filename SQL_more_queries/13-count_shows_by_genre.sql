-- we use where command inside a where command to take information out of other tables
SELECT tv_genres.name,COUNT(*) as occurence 
FROM tv_genres,tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY  occurence DESC;
