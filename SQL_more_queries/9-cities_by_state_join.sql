-- we use where command inside a where command to take information out of other tables
SELECT cities.id, cities.name,states.name 
FROM cities,states 
WHERE cities.state_id=states.id
ORDER BY id ASC
