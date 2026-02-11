-- WE USE TWO LEFT JOINS TO LINK ALL TABLES TOGETHER FROM AN ID VIEWPOINT AND ALSO SHOW MOVIES WITH NO GENRES 
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

