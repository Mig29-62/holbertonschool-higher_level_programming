-- we use where command inside a where command to take information out of other tables
select tv_genres.name,COUNT(*) as occurence 
from tv_genres,tv_shows
left join tv_show_genres
on tv_shows.id=tv_show_genres.show_id
where tv_show_genres.genre_id is not null
order by  occurence DESC;
