-- WE USE SELECT WITH DISTINCT TO OVERCOME REPEATING SAME GENRE NAME AND WRITE OUT A CONDITION AS PER HOLBERTON TASK RULES.
SELECT tv_shows.title,tv_genres.name
FROM tv_genres,tv_shows
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id;
ORDER BY tv_shows.title ASC,tv_genres.name ASC;
