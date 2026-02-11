-- WE USE SELECT WITH DISTINCT TO OVERCOME REPEATING SAME GENRE NAME AND WRITE OUT A CONDITION AS PER HOLBERTON TASK RULES.
SELECT DISTINCT tv_genres.name AS name
FROM tv_genres,tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id=tv_shows.id
WHERE tv_shows.title='Dexter'
ORDER BY tv_genres.name ASC; 
